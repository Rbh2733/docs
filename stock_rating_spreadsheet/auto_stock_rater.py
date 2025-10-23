#!/usr/bin/env python3
"""
Automated 3-Tier Stock Rating System
Fetches real-time data and calculates scores automatically
"""

import yfinance as yf
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import csv
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')


class StockDataFetcher:
    """Fetches stock data from Yahoo Finance"""

    def __init__(self):
        self.cache = {}

    def get_stock_data(self, symbol: str) -> Dict:
        """Fetch comprehensive stock data"""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info
            hist = ticker.history(period="2y")

            data = {
                'symbol': symbol,
                'price': info.get('currentPrice', info.get('regularMarketPrice', 0)),
                'market_cap': info.get('marketCap', 0) / 1e9,  # in billions
                'forward_pe': info.get('forwardPE', None),
                'trailing_pe': info.get('trailingPE', None),
                'peg_ratio': info.get('pegRatio', None),
                'price_to_sales': info.get('priceToSalesTrailing12Months', None),
                'revenue_growth': info.get('revenueGrowth', None),
                'earnings_growth': info.get('earningsGrowth', None),
                'operating_margins': info.get('operatingMargins', None),
                'profit_margins': info.get('profitMargins', None),
                'gross_margins': info.get('grossMargins', None),
                'roe': info.get('returnOnEquity', None),
                'roa': info.get('returnOnAssets', None),
                'free_cash_flow': info.get('freeCashflow', 0) / 1e9,  # in billions
                'total_cash': info.get('totalCash', 0) / 1e9,
                'total_debt': info.get('totalDebt', 0) / 1e9,
                'revenue': info.get('totalRevenue', 0) / 1e9,
                'beta': info.get('beta', 1.0),
                'fifty_day_avg': info.get('fiftyDayAverage', 0),
                'two_hundred_day_avg': info.get('twoHundredDayAverage', 0),
                'sector': info.get('sector', 'Unknown'),
                'industry': info.get('industry', 'Unknown'),
            }

            # Calculate price returns
            if len(hist) > 0:
                current_price = hist['Close'].iloc[-1]

                # 12-month return (excluding last month)
                if len(hist) >= 252:
                    price_12m_ago = hist['Close'].iloc[-252]
                    data['return_12m'] = ((current_price - price_12m_ago) / price_12m_ago) * 100

                # 6-month return
                if len(hist) >= 126:
                    price_6m_ago = hist['Close'].iloc[-126]
                    data['return_6m'] = ((current_price - price_6m_ago) / price_6m_ago) * 100

                # 3-month return
                if len(hist) >= 63:
                    price_3m_ago = hist['Close'].iloc[-63]
                    data['return_3m'] = ((current_price - price_3m_ago) / price_3m_ago) * 100

            # Get benchmark (QQQ) for relative strength
            qqq = yf.Ticker('QQQ')
            qqq_hist = qqq.history(period="1y")
            if len(qqq_hist) >= 252:
                qqq_return = ((qqq_hist['Close'].iloc[-1] - qqq_hist['Close'].iloc[-252]) /
                             qqq_hist['Close'].iloc[-252]) * 100
                data['qqq_return'] = qqq_return

            return data

        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            return None


class Tier1Scorer:
    """Score stocks for Tier 1 (Core)"""

    @staticmethod
    def score_pe_ratio(forward_pe: float, historical_avg_pe: float = None) -> int:
        """Score P/E ratio (0-100)"""
        if forward_pe is None or forward_pe <= 0:
            return 50

        # If no historical average, use general thresholds
        if historical_avg_pe is None:
            if forward_pe < 15:
                return 100
            elif forward_pe < 20:
                return 90
            elif forward_pe < 25:
                return 80
            elif forward_pe < 30:
                return 70
            elif forward_pe < 40:
                return 60
            else:
                return 40

        # Compare to historical average
        ratio = forward_pe / historical_avg_pe
        if ratio < 0.9:
            return 100
        elif ratio < 1.0:
            return 90
        else:
            score = 100 - ((ratio - 1) * 100)
            return max(30, min(100, int(score)))

    @staticmethod
    def score_fcf_yield(fcf: float, market_cap: float) -> int:
        """Score Free Cash Flow Yield (0-100)"""
        if market_cap == 0 or fcf <= 0:
            return 20

        fcf_yield = (fcf / market_cap) * 100

        if fcf_yield > 6:
            return 100
        elif fcf_yield > 4:
            return 80
        elif fcf_yield > 2:
            return 60
        elif fcf_yield > 0:
            return 40
        else:
            return 20

    @staticmethod
    def score_peg_ratio(peg: float) -> int:
        """Score PEG ratio (0-100)"""
        if peg is None:
            return 50

        if peg < 1.0:
            return 100
        elif peg < 1.5:
            return 85
        elif peg < 2.0:
            return 70
        elif peg < 2.5:
            return 50
        else:
            return 30

    @staticmethod
    def score_operating_margin(margin: float) -> int:
        """Score Operating Margin (0-100)"""
        if margin is None:
            return 50

        margin_pct = margin * 100

        if margin_pct > 30:
            return 100
        elif margin_pct > 20:
            return 85
        elif margin_pct > 15:
            return 70
        elif margin_pct > 10:
            return 50
        else:
            return 30

    @staticmethod
    def score_roe(roe: float) -> int:
        """Score Return on Equity as proxy for ROIC (0-100)"""
        if roe is None:
            return 50

        roe_pct = roe * 100

        if roe_pct > 25:
            return 100
        elif roe_pct > 20:
            return 90
        elif roe_pct > 15:
            return 75
        elif roe_pct > 10:
            return 50
        else:
            return 25

    @staticmethod
    def score_revenue_growth(growth: float) -> int:
        """Score Revenue Growth (0-100)"""
        if growth is None:
            return 50

        growth_pct = growth * 100

        if growth_pct > 25:
            return 100
        elif growth_pct > 20:
            return 90
        elif growth_pct > 15:
            return 75
        elif growth_pct > 10:
            return 55
        elif growth_pct > 5:
            return 35
        else:
            return 15

    @staticmethod
    def score_price_momentum(return_12m: float) -> int:
        """Score 12-month price return (0-100)"""
        if return_12m is None:
            return 50

        if return_12m > 40:
            return 100
        elif return_12m > 20:
            return 80
        elif return_12m > 0:
            return 60
        elif return_12m > -10:
            return 40
        else:
            return 60  # Potential reversal

    @staticmethod
    def score_relative_strength(stock_return: float, benchmark_return: float) -> int:
        """Score relative strength vs benchmark (0-100)"""
        if stock_return is None or benchmark_return is None:
            return 50

        outperformance = stock_return - benchmark_return

        if outperformance > 15:
            return 100
        elif outperformance > 0:
            return 75
        elif outperformance > -15:
            return 50
        else:
            return 30

    @staticmethod
    def score_technical(price: float, ma_50: float, ma_200: float) -> int:
        """Score technical setup (0-100)"""
        if price == 0 or ma_200 == 0:
            return 50

        above_200 = price > ma_200
        above_50 = price > ma_50

        if above_50 and above_200:
            return 100
        elif above_200:
            return 70
        elif above_50:
            return 50
        else:
            return 30

    @staticmethod
    def score_net_cash(total_cash: float, total_debt: float, market_cap: float) -> int:
        """Score net cash position (0-100)"""
        net_cash = total_cash - total_debt

        if net_cash > 50:
            return 100
        elif net_cash > 25:
            return 90
        elif net_cash > 0:
            return 80
        elif net_cash > -50:
            return 70
        else:
            return 50

    @classmethod
    def calculate_composite_score(cls, data: Dict) -> Dict:
        """Calculate all component scores and composite"""

        # Valuation (20%)
        pe_score = cls.score_pe_ratio(data.get('forward_pe'))
        fcf_yield_score = cls.score_fcf_yield(data.get('free_cash_flow', 0), data.get('market_cap', 1))
        peg_score = cls.score_peg_ratio(data.get('peg_ratio'))
        valuation_avg = np.mean([pe_score, fcf_yield_score, peg_score])

        # Quality (30%)
        roe_score = cls.score_roe(data.get('roe'))
        margin_score = cls.score_operating_margin(data.get('operating_margins'))
        moat_score = 70  # Default, needs manual assessment
        quality_avg = np.mean([roe_score, margin_score, moat_score])

        # Growth (30%)
        revenue_growth_score = cls.score_revenue_growth(data.get('revenue_growth'))
        earnings_growth_score = cls.score_revenue_growth(data.get('earnings_growth', data.get('revenue_growth')))
        growth_avg = np.mean([revenue_growth_score, earnings_growth_score])

        # Momentum (10%)
        momentum_score = cls.score_price_momentum(data.get('return_12m'))
        rel_strength_score = cls.score_relative_strength(data.get('return_12m'), data.get('qqq_return', 0))
        technical_score = cls.score_technical(data.get('price', 0), data.get('fifty_day_avg', 0),
                                              data.get('two_hundred_day_avg', 0))
        momentum_avg = np.mean([momentum_score, rel_strength_score, technical_score])

        # Financial Health (10%)
        net_cash_score = cls.score_net_cash(data.get('total_cash', 0), data.get('total_debt', 0),
                                            data.get('market_cap', 1))
        fcf_gen_score = 100 if data.get('free_cash_flow', 0) > 15 else 70
        financial_health_avg = np.mean([net_cash_score, fcf_gen_score])

        # Composite Score (weighted average)
        composite = (valuation_avg * 0.20 +
                    quality_avg * 0.30 +
                    growth_avg * 0.30 +
                    momentum_avg * 0.10 +
                    financial_health_avg * 0.10)

        # Rating
        if composite >= 85:
            rating = "Strong Buy ⭐⭐⭐⭐⭐"
        elif composite >= 75:
            rating = "Buy ⭐⭐⭐⭐"
        elif composite >= 65:
            rating = "Hold ⭐⭐⭐"
        elif composite >= 50:
            rating = "Reduce ⭐⭐"
        else:
            rating = "Sell ⭐"

        return {
            'valuation_score': round(valuation_avg, 1),
            'quality_score': round(quality_avg, 1),
            'growth_score': round(growth_avg, 1),
            'momentum_score': round(momentum_avg, 1),
            'financial_health_score': round(financial_health_avg, 1),
            'composite_score': round(composite, 1),
            'rating': rating,
            'pe_score': pe_score,
            'fcf_yield_score': fcf_yield_score,
            'peg_score': peg_score,
            'roe_score': roe_score,
            'margin_score': margin_score,
            'revenue_growth_score': revenue_growth_score,
            'momentum_raw_score': momentum_score,
            'relative_strength_score': rel_strength_score,
            'technical_score': technical_score,
        }


class Tier2Scorer:
    """Score stocks for Tier 2 (Emerging)"""

    @staticmethod
    def score_price_to_sales(ps_ratio: float) -> int:
        """Score P/S ratio for emerging companies (0-100)"""
        if ps_ratio is None:
            return 50

        if ps_ratio < 8:
            return 100
        elif ps_ratio < 15:
            return 80
        elif ps_ratio < 25:
            return 60
        else:
            return 40

    @staticmethod
    def score_gross_margin(margin: float) -> int:
        """Score Gross Margin (0-100)"""
        if margin is None:
            return 50

        margin_pct = margin * 100

        if margin_pct > 75:
            return 100
        elif margin_pct > 60:
            return 90
        elif margin_pct > 45:
            return 75
        elif margin_pct > 30:
            return 60
        else:
            return 40

    @staticmethod
    def score_high_growth_revenue(growth: float) -> int:
        """Score Revenue Growth for high-growth companies (0-100)"""
        if growth is None:
            return 50

        growth_pct = growth * 100

        if growth_pct > 40:
            return 100
        elif growth_pct > 30:
            return 90
        elif growth_pct > 25:
            return 80
        elif growth_pct > 20:
            return 70
        elif growth_pct > 15:
            return 55
        elif growth_pct > 10:
            return 40
        else:
            return 20

    @classmethod
    def calculate_composite_score(cls, data: Dict) -> Dict:
        """Calculate all component scores for Tier 2"""

        # Valuation (18%)
        ps_score = cls.score_price_to_sales(data.get('price_to_sales'))
        peg_score = Tier1Scorer.score_peg_ratio(data.get('peg_ratio'))
        valuation_avg = np.mean([ps_score, peg_score])

        # Quality (25%)
        revenue_size_score = 85 if data.get('revenue', 0) > 2 else 70
        gross_margin_score = cls.score_gross_margin(data.get('gross_margins'))
        margin_score = Tier1Scorer.score_operating_margin(data.get('operating_margins'))
        quality_avg = np.mean([revenue_size_score, gross_margin_score, margin_score])

        # Growth (35%) - HIGHEST WEIGHT
        revenue_growth_score = cls.score_high_growth_revenue(data.get('revenue_growth'))
        tam_score = 85  # Default, needs manual assessment
        growth_avg = np.mean([revenue_growth_score, tam_score])

        # Momentum (15%)
        momentum_score = Tier1Scorer.score_price_momentum(data.get('return_6m', data.get('return_12m')))
        rel_strength_score = Tier1Scorer.score_relative_strength(data.get('return_6m'), data.get('qqq_return', 0))
        momentum_avg = np.mean([momentum_score, rel_strength_score])

        # Scale & Moat (7%)
        moat_score = 75  # Default

        # Composite Score
        composite = (valuation_avg * 0.18 +
                    quality_avg * 0.25 +
                    growth_avg * 0.35 +
                    momentum_avg * 0.15 +
                    moat_score * 0.07)

        # Rating
        if composite >= 85:
            rating = "Strong Buy ⭐⭐⭐⭐⭐"
        elif composite >= 75:
            rating = "Buy ⭐⭐⭐⭐"
        elif composite >= 65:
            rating = "Hold ⭐⭐⭐"
        elif composite >= 50:
            rating = "Reduce ⭐⭐"
        else:
            rating = "Sell ⭐"

        return {
            'valuation_score': round(valuation_avg, 1),
            'quality_score': round(quality_avg, 1),
            'growth_score': round(growth_avg, 1),
            'momentum_score': round(momentum_avg, 1),
            'moat_score': moat_score,
            'composite_score': round(composite, 1),
            'rating': rating,
        }


class Tier3Scorer:
    """Score stocks for Tier 3 (Moonshots)"""

    @staticmethod
    def score_hypergrowth_revenue(growth: float) -> int:
        """Score Revenue Growth for moonshots (0-100)"""
        if growth is None:
            return 50

        growth_pct = growth * 100

        if growth_pct > 100:
            return 100
        elif growth_pct > 75:
            return 95
        elif growth_pct > 50:
            return 85
        elif growth_pct > 30:
            return 70
        elif growth_pct > 20:
            return 50
        else:
            return 25

    @classmethod
    def calculate_composite_score(cls, data: Dict) -> Dict:
        """Calculate all component scores for Tier 3"""

        # Valuation (10%) - LOWEST WEIGHT
        ps_score = Tier2Scorer.score_price_to_sales(data.get('price_to_sales'))
        valuation_avg = ps_score

        # Quality (15%)
        gross_margin_score = Tier2Scorer.score_gross_margin(data.get('gross_margins'))
        quality_avg = gross_margin_score

        # Growth (45%) - HIGHEST WEIGHT
        revenue_growth_score = cls.score_hypergrowth_revenue(data.get('revenue_growth'))
        tam_score = 90  # Default for moonshots
        growth_avg = np.mean([revenue_growth_score, tam_score])

        # Momentum (20%)
        momentum_score = 90 if data.get('return_6m', 0) > 50 else 70

        # Disruption (10%)
        disruption_score = 80  # Default, needs manual assessment

        # Composite Score
        composite = (valuation_avg * 0.10 +
                    quality_avg * 0.15 +
                    growth_avg * 0.45 +
                    momentum_score * 0.20 +
                    disruption_score * 0.10)

        # Rating
        if composite >= 85:
            rating = "Strong Buy ⭐⭐⭐⭐⭐"
        elif composite >= 75:
            rating = "Buy ⭐⭐⭐⭐"
        elif composite >= 65:
            rating = "Hold ⭐⭐⭐"
        else:
            rating = "High Risk ⭐⭐"

        # Calculate stop loss
        stop_loss_price = data.get('price', 0) * 0.6

        return {
            'valuation_score': round(valuation_avg, 1),
            'quality_score': round(quality_avg, 1),
            'growth_score': round(growth_avg, 1),
            'momentum_score': momentum_score,
            'disruption_score': disruption_score,
            'composite_score': round(composite, 1),
            'rating': rating,
            'stop_loss_price': round(stop_loss_price, 2),
        }


class AutomatedRater:
    """Main automation class"""

    def __init__(self, config_file: str = "watchlist.json"):
        self.fetcher = StockDataFetcher()
        self.config_file = config_file
        self.results = {
            'tier1': [],
            'tier2': [],
            'tier3': [],
            'timestamp': datetime.now().isoformat()
        }

    def load_watchlist(self) -> Dict:
        """Load stock watchlist from config file"""
        try:
            with open(self.config_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            # Create default watchlist
            default = {
                'tier1': ['GOOGL', 'AAPL', 'MSFT', 'NVDA', 'META'],
                'tier2': ['PLTR', 'SNOW', 'DDOG', 'CRWD', 'NET'],
                'tier3': ['RKLB', 'IONQ', 'HOOD', 'SOFI', 'COIN']
            }
            with open(self.config_file, 'w') as f:
                json.dump(default, f, indent=2)
            print(f"Created default watchlist: {self.config_file}")
            return default

    def rate_all_stocks(self):
        """Fetch and rate all stocks in watchlist"""
        watchlist = self.load_watchlist()

        print(f"\n{'='*80}")
        print(f"AUTOMATED STOCK RATING - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"{'='*80}\n")

        # Process Tier 1
        print("TIER 1 (CORE) STOCKS:")
        print("-" * 80)
        for symbol in watchlist.get('tier1', []):
            data = self.fetcher.get_stock_data(symbol)
            if data:
                scores = Tier1Scorer.calculate_composite_score(data)
                result = {**data, **scores}
                self.results['tier1'].append(result)
                self._print_stock_summary(result, 'Tier 1')

        print("\n" + "="*80 + "\n")

        # Process Tier 2
        print("TIER 2 (EMERGING) STOCKS:")
        print("-" * 80)
        for symbol in watchlist.get('tier2', []):
            data = self.fetcher.get_stock_data(symbol)
            if data:
                scores = Tier2Scorer.calculate_composite_score(data)
                result = {**data, **scores}
                self.results['tier2'].append(result)
                self._print_stock_summary(result, 'Tier 2')

        print("\n" + "="*80 + "\n")

        # Process Tier 3
        print("TIER 3 (MOONSHOTS) STOCKS:")
        print("-" * 80)
        for symbol in watchlist.get('tier3', []):
            data = self.fetcher.get_stock_data(symbol)
            if data:
                scores = Tier3Scorer.calculate_composite_score(data)
                result = {**data, **scores}
                self.results['tier3'].append(result)
                self._print_stock_summary(result, 'Tier 3')

        print("\n" + "="*80)

    def _print_stock_summary(self, data: Dict, tier: str):
        """Print formatted stock summary"""
        symbol = data['symbol']
        price = data.get('price', 0)
        composite = data.get('composite_score', 0)
        rating = data.get('rating', 'N/A')

        print(f"{symbol:6} ${price:7.2f}  Score: {composite:5.1f}  {rating}")

    def export_to_csv(self, output_dir: str = "."):
        """Export results to CSV files"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        # Export Tier 1
        if self.results['tier1']:
            filename = f"{output_dir}/tier1_scores_{timestamp}.csv"
            self._export_tier_csv(self.results['tier1'], filename, 'tier1')
            print(f"\nExported Tier 1 results to: {filename}")

        # Export Tier 2
        if self.results['tier2']:
            filename = f"{output_dir}/tier2_scores_{timestamp}.csv"
            self._export_tier_csv(self.results['tier2'], filename, 'tier2')
            print(f"Exported Tier 2 results to: {filename}")

        # Export Tier 3
        if self.results['tier3']:
            filename = f"{output_dir}/tier3_scores_{timestamp}.csv"
            self._export_tier_csv(self.results['tier3'], filename, 'tier3')
            print(f"Exported Tier 3 results to: {filename}")

    def _export_tier_csv(self, data: List[Dict], filename: str, tier: str):
        """Export tier data to CSV"""
        if not data:
            return

        with open(filename, 'w', newline='') as f:
            if tier == 'tier1':
                fieldnames = ['symbol', 'price', 'market_cap', 'valuation_score', 'quality_score',
                            'growth_score', 'momentum_score', 'financial_health_score',
                            'composite_score', 'rating', 'forward_pe', 'peg_ratio',
                            'revenue_growth', 'operating_margins', 'free_cash_flow']
            elif tier == 'tier2':
                fieldnames = ['symbol', 'price', 'market_cap', 'valuation_score', 'quality_score',
                            'growth_score', 'momentum_score', 'moat_score', 'composite_score',
                            'rating', 'price_to_sales', 'revenue_growth', 'gross_margins']
            else:  # tier3
                fieldnames = ['symbol', 'price', 'market_cap', 'valuation_score', 'quality_score',
                            'growth_score', 'momentum_score', 'disruption_score', 'composite_score',
                            'rating', 'stop_loss_price', 'price_to_sales', 'revenue_growth']

            writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(data)

    def generate_alerts(self) -> List[str]:
        """Generate alerts for action items"""
        alerts = []

        # Check for Strong Buy opportunities
        for tier_name, stocks in [('Tier 1', self.results['tier1']),
                                   ('Tier 2', self.results['tier2']),
                                   ('Tier 3', self.results['tier3'])]:
            for stock in stocks:
                if stock['composite_score'] >= 85:
                    alerts.append(f"⭐ {tier_name} STRONG BUY: {stock['symbol']} - Score: {stock['composite_score']}")

        # Check for Sell signals
        for tier_name, stocks in [('Tier 1', self.results['tier1']),
                                   ('Tier 2', self.results['tier2']),
                                   ('Tier 3', self.results['tier3'])]:
            for stock in stocks:
                if stock['composite_score'] < 65:
                    alerts.append(f"⚠️  {tier_name} REVIEW: {stock['symbol']} - Score: {stock['composite_score']} ({stock['rating']})")

        # Check Tier 3 stop losses
        for stock in self.results['tier3']:
            if 'stop_loss_price' in stock:
                if stock['price'] <= stock['stop_loss_price']:
                    alerts.append(f"🛑 STOP LOSS HIT: {stock['symbol']} - Price: ${stock['price']:.2f}, Stop: ${stock['stop_loss_price']:.2f}")

        return alerts

    def print_summary(self):
        """Print portfolio summary"""
        print("\n" + "="*80)
        print("PORTFOLIO SUMMARY")
        print("="*80)

        total_stocks = len(self.results['tier1']) + len(self.results['tier2']) + len(self.results['tier3'])
        print(f"\nTotal stocks rated: {total_stocks}")
        print(f"  Tier 1 (Core): {len(self.results['tier1'])}")
        print(f"  Tier 2 (Emerging): {len(self.results['tier2'])}")
        print(f"  Tier 3 (Moonshots): {len(self.results['tier3'])}")

        # Calculate average scores
        if self.results['tier1']:
            avg_tier1 = np.mean([s['composite_score'] for s in self.results['tier1']])
            print(f"\nAverage Tier 1 Score: {avg_tier1:.1f}")

        if self.results['tier2']:
            avg_tier2 = np.mean([s['composite_score'] for s in self.results['tier2']])
            print(f"Average Tier 2 Score: {avg_tier2:.1f}")

        if self.results['tier3']:
            avg_tier3 = np.mean([s['composite_score'] for s in self.results['tier3']])
            print(f"Average Tier 3 Score: {avg_tier3:.1f}")

        # Print alerts
        alerts = self.generate_alerts()
        if alerts:
            print("\n" + "="*80)
            print("ALERTS & ACTION ITEMS")
            print("="*80)
            for alert in alerts:
                print(alert)

        print("\n" + "="*80)


def main():
    """Main execution function"""
    import sys

    print("🤖 Automated Stock Rating System")
    print("Fetching real-time data and calculating scores...")

    # Initialize rater
    rater = AutomatedRater()

    # Rate all stocks
    rater.rate_all_stocks()

    # Print summary
    rater.print_summary()

    # Export to CSV
    rater.export_to_csv()

    # Generate HTML dashboard
    try:
        from dashboard_generator import generate_html_dashboard
        generate_html_dashboard(rater.results)
    except ImportError:
        print("\nNote: Install jinja2 for HTML dashboard generation")
    except Exception as e:
        print(f"\nNote: Could not generate HTML dashboard: {e}")

    print("\n✅ Automation complete!")
    print("\nNext steps:")
    print("1. Review the generated CSV files")
    print("2. Open dashboard.html in your browser")
    print("3. Check alerts for action items")
    print("4. Update your positions based on scores")
    print("5. Run this script daily/weekly for updates")
    print("\nTip: Use scheduler.py to automate regular updates")


if __name__ == "__main__":
    main()
