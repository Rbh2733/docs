#!/usr/bin/env python3
"""
HTML Dashboard Generator for Stock Rating System
Creates interactive HTML dashboard with charts
"""

from datetime import datetime
from typing import Dict, List
import json


def generate_html_dashboard(results: Dict, output_file: str = "dashboard.html"):
    """Generate an interactive HTML dashboard"""

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3-Tier Stock Rating Dashboard</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            color: #333;
        }}

        .container {{
            max-width: 1400px;
            margin: 0 auto;
        }}

        header {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
            text-align: center;
        }}

        h1 {{
            color: #667eea;
            margin-bottom: 10px;
            font-size: 2.5em;
        }}

        .timestamp {{
            color: #666;
            font-size: 0.9em;
        }}

        .summary-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-bottom: 30px;
        }}

        .summary-card {{
            background: white;
            padding: 25px;
            border-radius: 15px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            text-align: center;
        }}

        .summary-card h3 {{
            color: #667eea;
            margin-bottom: 10px;
            font-size: 1em;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        .summary-card .number {{
            font-size: 3em;
            font-weight: bold;
            color: #333;
        }}

        .tier-section {{
            background: white;
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            margin-bottom: 30px;
        }}

        .tier-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 25px;
            padding-bottom: 15px;
            border-bottom: 3px solid #667eea;
        }}

        .tier-title {{
            font-size: 1.8em;
            color: #667eea;
            font-weight: bold;
        }}

        .tier-badge {{
            background: #667eea;
            color: white;
            padding: 8px 20px;
            border-radius: 25px;
            font-size: 0.9em;
            font-weight: bold;
        }}

        table {{
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }}

        thead {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }}

        th {{
            padding: 15px;
            text-align: left;
            font-weight: 600;
            text-transform: uppercase;
            font-size: 0.85em;
            letter-spacing: 0.5px;
        }}

        td {{
            padding: 15px;
            border-bottom: 1px solid #eee;
        }}

        tbody tr:hover {{
            background: #f8f9fa;
            transition: background 0.2s;
        }}

        .stock-symbol {{
            font-weight: bold;
            font-size: 1.1em;
            color: #667eea;
        }}

        .score {{
            font-weight: bold;
            padding: 5px 12px;
            border-radius: 5px;
            display: inline-block;
        }}

        .score-excellent {{
            background: #10b981;
            color: white;
        }}

        .score-good {{
            background: #3b82f6;
            color: white;
        }}

        .score-moderate {{
            background: #f59e0b;
            color: white;
        }}

        .score-poor {{
            background: #ef4444;
            color: white;
        }}

        .rating {{
            font-size: 1.1em;
        }}

        .alerts {{
            background: #fff3cd;
            border-left: 5px solid #ffc107;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 30px;
        }}

        .alerts h3 {{
            color: #856404;
            margin-bottom: 15px;
        }}

        .alert-item {{
            padding: 10px;
            margin: 5px 0;
            background: white;
            border-radius: 5px;
            font-size: 0.95em;
        }}

        .alert-buy {{
            border-left: 4px solid #10b981;
        }}

        .alert-warning {{
            border-left: 4px solid #f59e0b;
        }}

        .alert-danger {{
            border-left: 4px solid #ef4444;
        }}

        footer {{
            text-align: center;
            color: white;
            margin-top: 30px;
            padding: 20px;
            font-size: 0.9em;
        }}

        .progress-bar {{
            width: 100%;
            height: 8px;
            background: #e5e7eb;
            border-radius: 10px;
            overflow: hidden;
            margin-top: 10px;
        }}

        .progress-fill {{
            height: 100%;
            background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
            transition: width 0.3s;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📊 3-Tier Stock Rating Dashboard</h1>
            <p class="timestamp">Last Updated: {timestamp}</p>
        </header>
"""

    # Calculate summary statistics
    tier1_count = len(results.get('tier1', []))
    tier2_count = len(results.get('tier2', []))
    tier3_count = len(results.get('tier3', []))
    total_stocks = tier1_count + tier2_count + tier3_count

    # Calculate average scores
    tier1_avg = sum([s['composite_score'] for s in results.get('tier1', [])]) / max(tier1_count, 1)
    tier2_avg = sum([s['composite_score'] for s in results.get('tier2', [])]) / max(tier2_count, 1)
    tier3_avg = sum([s['composite_score'] for s in results.get('tier3', [])]) / max(tier3_count, 1)

    # Summary cards
    html += f"""
        <div class="summary-grid">
            <div class="summary-card">
                <h3>Total Stocks</h3>
                <div class="number">{total_stocks}</div>
            </div>
            <div class="summary-card">
                <h3>Tier 1 Avg Score</h3>
                <div class="number">{tier1_avg:.1f}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {tier1_avg}%"></div>
                </div>
            </div>
            <div class="summary-card">
                <h3>Tier 2 Avg Score</h3>
                <div class="number">{tier2_avg:.1f}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {tier2_avg}%"></div>
                </div>
            </div>
            <div class="summary-card">
                <h3>Tier 3 Avg Score</h3>
                <div class="number">{tier3_avg:.1f}</div>
                <div class="progress-bar">
                    <div class="progress-fill" style="width: {tier3_avg}%"></div>
                </div>
            </div>
        </div>
"""

    # Generate alerts
    alerts = generate_alerts(results)
    if alerts:
        html += """
        <div class="alerts">
            <h3>⚡ Alerts & Action Items</h3>
"""
        for alert in alerts:
            if "STRONG BUY" in alert:
                alert_class = "alert-buy"
            elif "STOP LOSS" in alert:
                alert_class = "alert-danger"
            else:
                alert_class = "alert-warning"

            html += f'            <div class="alert-item {alert_class}">{alert}</div>\n'

        html += """
        </div>
"""

    # Tier 1 Section
    html += generate_tier_table("Tier 1 (Core)", "45% Target | 15% Max Position",
                                results.get('tier1', []), 'tier1')

    # Tier 2 Section
    html += generate_tier_table("Tier 2 (Emerging)", "30% Target | 8% Max Position",
                                results.get('tier2', []), 'tier2')

    # Tier 3 Section
    html += generate_tier_table("Tier 3 (Moonshots)", "20% Target | 3% Max Position",
                                results.get('tier3', []), 'tier3')

    # Footer
    html += f"""
        <footer>
            <p>🤖 Generated with Automated Stock Rating System</p>
            <p>Data provided by Yahoo Finance via yfinance</p>
        </footer>
    </div>
</body>
</html>
"""

    # Write to file
    with open(output_file, 'w') as f:
        f.write(html)

    print(f"\n📊 Dashboard generated: {output_file}")
    return output_file


def generate_tier_table(title: str, subtitle: str, stocks: List[Dict], tier: str) -> str:
    """Generate HTML table for a tier"""
    if not stocks:
        return ""

    html = f"""
        <div class="tier-section">
            <div class="tier-header">
                <div class="tier-title">{title}</div>
                <div class="tier-badge">{subtitle}</div>
            </div>
            <table>
                <thead>
                    <tr>
                        <th>Symbol</th>
                        <th>Price</th>
                        <th>Market Cap</th>
                        <th>Composite Score</th>
                        <th>Rating</th>
                        <th>Valuation</th>
                        <th>Quality</th>
                        <th>Growth</th>
                        <th>Momentum</th>
"""

    if tier == 'tier1':
        html += "                        <th>Fin Health</th>\n"
    elif tier == 'tier2':
        html += "                        <th>Moat</th>\n"
    else:  # tier3
        html += "                        <th>Disruption</th>\n"

    html += """
                    </tr>
                </thead>
                <tbody>
"""

    for stock in sorted(stocks, key=lambda x: x['composite_score'], reverse=True):
        score_class = get_score_class(stock['composite_score'])
        market_cap_str = f"${stock.get('market_cap', 0):.1f}B"

        html += f"""
                    <tr>
                        <td class="stock-symbol">{stock['symbol']}</td>
                        <td>${stock.get('price', 0):.2f}</td>
                        <td>{market_cap_str}</td>
                        <td><span class="score {score_class}">{stock['composite_score']:.1f}</span></td>
                        <td class="rating">{stock['rating']}</td>
                        <td>{stock.get('valuation_score', 0):.1f}</td>
                        <td>{stock.get('quality_score', 0):.1f}</td>
                        <td>{stock.get('growth_score', 0):.1f}</td>
                        <td>{stock.get('momentum_score', 0):.1f}</td>
"""

        if tier == 'tier1':
            html += f"                        <td>{stock.get('financial_health_score', 0):.1f}</td>\n"
        elif tier == 'tier2':
            html += f"                        <td>{stock.get('moat_score', 0):.1f}</td>\n"
        else:
            html += f"                        <td>{stock.get('disruption_score', 0):.1f}</td>\n"

        html += "                    </tr>\n"

    html += """
                </tbody>
            </table>
        </div>
"""

    return html


def get_score_class(score: float) -> str:
    """Get CSS class based on score"""
    if score >= 85:
        return "score-excellent"
    elif score >= 75:
        return "score-good"
    elif score >= 65:
        return "score-moderate"
    else:
        return "score-poor"


def generate_alerts(results: Dict) -> List[str]:
    """Generate alerts from results"""
    alerts = []

    # Strong Buy opportunities
    for tier_name, stocks in [('Tier 1', results.get('tier1', [])),
                               ('Tier 2', results.get('tier2', [])),
                               ('Tier 3', results.get('tier3', []))]:
        for stock in stocks:
            if stock['composite_score'] >= 85:
                alerts.append(f"⭐ {tier_name} STRONG BUY: {stock['symbol']} - Score: {stock['composite_score']:.1f}")

    # Review needed
    for tier_name, stocks in [('Tier 1', results.get('tier1', [])),
                               ('Tier 2', results.get('tier2', [])),
                               ('Tier 3', results.get('tier3', []))]:
        for stock in stocks:
            if stock['composite_score'] < 65:
                alerts.append(f"⚠️ {tier_name} REVIEW: {stock['symbol']} - Score: {stock['composite_score']:.1f} ({stock['rating']})")

    # Tier 3 stop losses
    for stock in results.get('tier3', []):
        if 'stop_loss_price' in stock:
            if stock['price'] <= stock['stop_loss_price']:
                alerts.append(f"🛑 STOP LOSS HIT: {stock['symbol']} - Price: ${stock['price']:.2f}, Stop: ${stock['stop_loss_price']:.2f}")

    return alerts


if __name__ == "__main__":
    # Example usage
    print("HTML Dashboard Generator")
    print("Import this module in auto_stock_rater.py to generate dashboards")
