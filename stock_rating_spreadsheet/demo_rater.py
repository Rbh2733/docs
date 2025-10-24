#!/usr/bin/env python3
"""
Demo version of auto_stock_rater.py
Simulates output with mock data (no external dependencies required)
"""

from datetime import datetime
import json

# Mock stock data
MOCK_DATA = {
    'tier1': {
        'GOOGL': {
            'symbol': 'GOOGL', 'price': 140.50, 'market_cap': 1800,
            'valuation_score': 72, 'quality_score': 95, 'growth_score': 70,
            'momentum_score': 90, 'financial_health_score': 100,
            'composite_score': 82.4, 'rating': 'Buy ⭐⭐⭐⭐'
        },
        'AAPL': {
            'symbol': 'AAPL', 'price': 178.25, 'market_cap': 2800,
            'valuation_score': 68, 'quality_score': 92, 'growth_score': 65,
            'momentum_score': 85, 'financial_health_score': 95,
            'composite_score': 79.1, 'rating': 'Buy ⭐⭐⭐⭐'
        },
        'MSFT': {
            'symbol': 'MSFT', 'price': 372.15, 'market_cap': 2750,
            'valuation_score': 75, 'quality_score': 98, 'growth_score': 75,
            'momentum_score': 92, 'financial_health_score': 98,
            'composite_score': 85.3, 'rating': 'Strong Buy ⭐⭐⭐⭐⭐'
        },
        'NVDA': {
            'symbol': 'NVDA', 'price': 495.20, 'market_cap': 1200,
            'valuation_score': 70, 'quality_score': 95, 'growth_score': 95,
            'momentum_score': 100, 'financial_health_score': 90,
            'composite_score': 88.7, 'rating': 'Strong Buy ⭐⭐⭐⭐⭐'
        },
        'META': {
            'symbol': 'META', 'price': 485.30, 'market_cap': 1250,
            'valuation_score': 78, 'quality_score': 88, 'growth_score': 72,
            'momentum_score': 88, 'financial_health_score': 92,
            'composite_score': 81.2, 'rating': 'Buy ⭐⭐⭐⭐'
        }
    },
    'tier2': {
        'PLTR': {
            'symbol': 'PLTR', 'price': 28.50, 'market_cap': 65,
            'valuation_score': 61, 'quality_score': 89, 'growth_score': 92,
            'momentum_score': 93, 'moat_score': 98,
            'composite_score': 86.4, 'rating': 'Strong Buy ⭐⭐⭐⭐⭐'
        },
        'SNOW': {
            'symbol': 'SNOW', 'price': 142.75, 'market_cap': 48,
            'valuation_score': 55, 'quality_score': 82, 'growth_score': 88,
            'momentum_score': 78, 'moat_score': 85,
            'composite_score': 78.5, 'rating': 'Buy ⭐⭐⭐⭐'
        },
        'DDOG': {
            'symbol': 'DDOG', 'price': 115.80, 'market_cap': 39,
            'valuation_score': 62, 'quality_score': 87, 'growth_score': 85,
            'momentum_score': 82, 'moat_score': 88,
            'composite_score': 80.9, 'rating': 'Buy ⭐⭐⭐⭐'
        },
        'CRWD': {
            'symbol': 'CRWD', 'price': 295.40, 'market_cap': 72,
            'valuation_score': 58, 'quality_score': 90, 'growth_score': 90,
            'momentum_score': 95, 'moat_score': 92,
            'composite_score': 84.2, 'rating': 'Buy ⭐⭐⭐⭐'
        },
        'NET': {
            'symbol': 'NET', 'price': 88.25, 'market_cap': 32,
            'valuation_score': 60, 'quality_score': 85, 'growth_score': 87,
            'momentum_score': 80, 'moat_score': 86,
            'composite_score': 79.8, 'rating': 'Buy ⭐⭐⭐⭐'
        }
    },
    'tier3': {
        'RKLB': {
            'symbol': 'RKLB', 'price': 9.50, 'market_cap': 4.5,
            'valuation_score': 78, 'quality_score': 75, 'growth_score': 94,
            'momentum_score': 96, 'disruption_score': 93,
            'composite_score': 89.9, 'rating': 'Strong Buy ⭐⭐⭐⭐⭐',
            'stop_loss_price': 5.70
        },
        'IONQ': {
            'symbol': 'IONQ', 'price': 12.35, 'market_cap': 2.8,
            'valuation_score': 55, 'quality_score': 65, 'growth_score': 95,
            'momentum_score': 88, 'disruption_score': 95,
            'composite_score': 85.2, 'rating': 'Strong Buy ⭐⭐⭐⭐⭐',
            'stop_loss_price': 7.41
        },
        'HOOD': {
            'symbol': 'HOOD', 'price': 28.90, 'market_cap': 25,
            'valuation_score': 62, 'quality_score': 70, 'growth_score': 82,
            'momentum_score': 85, 'disruption_score': 80,
            'composite_score': 78.3, 'rating': 'Buy ⭐⭐⭐⭐',
            'stop_loss_price': 17.34
        },
        'SOFI': {
            'symbol': 'SOFI', 'price': 10.85, 'market_cap': 11,
            'valuation_score': 68, 'quality_score': 72, 'growth_score': 80,
            'momentum_score': 78, 'disruption_score': 75,
            'composite_score': 76.1, 'rating': 'Buy ⭐⭐⭐⭐',
            'stop_loss_price': 6.51
        },
        'COIN': {
            'symbol': 'COIN', 'price': 235.40, 'market_cap': 58,
            'valuation_score': 45, 'quality_score': 62, 'growth_score': 70,
            'momentum_score': 72, 'disruption_score': 68,
            'composite_score': 64.8, 'rating': 'Hold ⭐⭐⭐',
            'stop_loss_price': 141.24
        }
    }
}

def print_header():
    """Print header"""
    print(f"\n{'='*80}")
    print(f"AUTOMATED STOCK RATING - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*80}\n")
    print("⚠️  DEMO MODE: Using mock data (install yfinance for real data)")
    print("")

def print_tier_stocks(tier_name, stocks):
    """Print stocks for a tier"""
    print(f"{'='*80}")
    print(f"{tier_name}:")
    print("-" * 80)
    for symbol, data in stocks.items():
        print(f"{symbol:6} ${data['price']:7.2f}  Score: {data['composite_score']:5.1f}  {data['rating']}")
    print("")

def print_summary(all_data):
    """Print summary"""
    print("="*80)
    print("PORTFOLIO SUMMARY")
    print("="*80)

    tier1_avg = sum(s['composite_score'] for s in all_data['tier1'].values()) / len(all_data['tier1'])
    tier2_avg = sum(s['composite_score'] for s in all_data['tier2'].values()) / len(all_data['tier2'])
    tier3_avg = sum(s['composite_score'] for s in all_data['tier3'].values()) / len(all_data['tier3'])

    total = len(all_data['tier1']) + len(all_data['tier2']) + len(all_data['tier3'])

    print(f"\nTotal stocks rated: {total}")
    print(f"  Tier 1 (Core): {len(all_data['tier1'])}")
    print(f"  Tier 2 (Emerging): {len(all_data['tier2'])}")
    print(f"  Tier 3 (Moonshots): {len(all_data['tier3'])}")

    print(f"\nAverage Tier 1 Score: {tier1_avg:.1f}")
    print(f"Average Tier 2 Score: {tier2_avg:.1f}")
    print(f"Average Tier 3 Score: {tier3_avg:.1f}")

def print_alerts(all_data):
    """Print alerts"""
    alerts = []

    # Strong Buy alerts
    for tier_name, stocks in [('Tier 1', all_data['tier1']),
                               ('Tier 2', all_data['tier2']),
                               ('Tier 3', all_data['tier3'])]:
        for symbol, data in stocks.items():
            if data['composite_score'] >= 85:
                alerts.append(f"⭐ {tier_name} STRONG BUY: {symbol} - Score: {data['composite_score']:.1f}")

    # Review alerts
    for tier_name, stocks in [('Tier 1', all_data['tier1']),
                               ('Tier 2', all_data['tier2']),
                               ('Tier 3', all_data['tier3'])]:
        for symbol, data in stocks.items():
            if data['composite_score'] < 65:
                alerts.append(f"⚠️  {tier_name} REVIEW: {symbol} - Score: {data['composite_score']:.1f} ({data['rating']})")

    if alerts:
        print("\n" + "="*80)
        print("ALERTS & ACTION ITEMS")
        print("="*80)
        for alert in alerts:
            print(alert)

def save_csv(tier_name, stocks, filename):
    """Save stocks to CSV"""
    import csv

    with open(filename, 'w', newline='') as f:
        if tier_name == 'tier1':
            fieldnames = ['symbol', 'price', 'market_cap', 'valuation_score', 'quality_score',
                        'growth_score', 'momentum_score', 'financial_health_score',
                        'composite_score', 'rating']
        elif tier_name == 'tier2':
            fieldnames = ['symbol', 'price', 'market_cap', 'valuation_score', 'quality_score',
                        'growth_score', 'momentum_score', 'moat_score', 'composite_score', 'rating']
        else:  # tier3
            fieldnames = ['symbol', 'price', 'market_cap', 'valuation_score', 'quality_score',
                        'growth_score', 'momentum_score', 'disruption_score', 'composite_score',
                        'rating', 'stop_loss_price']

        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(stocks.values())

def main():
    """Main execution"""
    print_header()

    # Print each tier
    print_tier_stocks("TIER 1 (CORE) STOCKS", MOCK_DATA['tier1'])
    print_tier_stocks("\nTIER 2 (EMERGING) STOCKS", MOCK_DATA['tier2'])
    print_tier_stocks("\nTIER 3 (MOONSHOTS) STOCKS", MOCK_DATA['tier3'])

    # Print summary
    print_summary(MOCK_DATA)

    # Print alerts
    print_alerts(MOCK_DATA)

    # Save CSV files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    save_csv('tier1', MOCK_DATA['tier1'], f'tier1_scores_{timestamp}.csv')
    save_csv('tier2', MOCK_DATA['tier2'], f'tier2_scores_{timestamp}.csv')
    save_csv('tier3', MOCK_DATA['tier3'], f'tier3_scores_{timestamp}.csv')

    print("\n" + "="*80)
    print(f"\n✅ Demo complete!")
    print(f"\nExported results:")
    print(f"  - tier1_scores_{timestamp}.csv")
    print(f"  - tier2_scores_{timestamp}.csv")
    print(f"  - tier3_scores_{timestamp}.csv")

    print("\n📊 To get real-time data:")
    print("  1. Install requirements: pip install yfinance pandas numpy")
    print("  2. Run: python3 auto_stock_rater.py")

    print("\n" + "="*80)

if __name__ == "__main__":
    main()
