#!/usr/bin/env python3
"""
3-Tier Stock Rating System Spreadsheet Generator
Creates a comprehensive Excel workbook with all scoring components
"""

import csv
import os

def create_config_weights():
    """Create the Config & Weights tab data"""
    data = [
        ["3-TIER STOCK RATING SYSTEM - CONFIGURATION", "", "", ""],
        ["", "", "", ""],
        ["PORTFOLIO ALLOCATION TARGETS", "", "", ""],
        ["Tier", "Target %", "Min %", "Max %"],
        ["Tier 1 (Core)", "45", "35", "55"],
        ["Tier 2 (Emerging)", "30", "20", "40"],
        ["Tier 3 (Moonshots)", "20", "10", "30"],
        ["Cash", "5", "0", "15"],
        ["TOTAL", "100", "", ""],
        ["", "", "", ""],
        ["TIER 1 (CORE) - COMPONENT WEIGHTS", "", "", ""],
        ["Component", "Weight %", "", ""],
        ["Valuation Score", "20", "", ""],
        ["Quality Score", "30", "", ""],
        ["Growth Score", "30", "", ""],
        ["Momentum Score", "10", "", ""],
        ["Financial Health Score", "10", "", ""],
        ["TOTAL", "100", "", ""],
        ["", "", "", ""],
        ["TIER 2 (EMERGING) - COMPONENT WEIGHTS", "", "", ""],
        ["Component", "Weight %", "", ""],
        ["Valuation Score", "18", "", ""],
        ["Quality Score", "25", "", ""],
        ["Growth Score", "35", "", ""],
        ["Momentum Score", "15", "", ""],
        ["Scale & Moat Score", "7", "", ""],
        ["TOTAL", "100", "", ""],
        ["", "", "", ""],
        ["TIER 3 (MOONSHOTS) - COMPONENT WEIGHTS", "", "", ""],
        ["Component", "Weight %", "", ""],
        ["Valuation Score", "10", "", ""],
        ["Quality Score", "15", "", ""],
        ["Growth Score", "45", "", ""],
        ["Momentum Score", "20", "", ""],
        ["Disruption Potential Score", "10", "", ""],
        ["TOTAL", "100", "", ""],
        ["", "", "", ""],
        ["RATING THRESHOLDS", "", "", ""],
        ["Composite Score", "Rating", "Action", "Stars"],
        ["85-100", "Strong Buy", "Add/Hold", "⭐⭐⭐⭐⭐"],
        ["75-84", "Buy", "Add/Hold", "⭐⭐⭐⭐"],
        ["65-74", "Hold", "Monitor", "⭐⭐⭐"],
        ["50-64", "Reduce", "Trim Position", "⭐⭐"],
        ["0-49", "Sell", "Exit Position", "⭐"],
        ["", "", "", ""],
        ["POSITION SIZING GUIDELINES", "", "", ""],
        ["Tier 1 Maximum Position Size", "15%", "", ""],
        ["Tier 2 Maximum Position Size", "8%", "", ""],
        ["Tier 3 Maximum Position Size", "3%", "", ""],
        ["", "", "", ""],
        ["RISK MANAGEMENT", "", "", ""],
        ["Tier 3 Stop Loss", "-40%", "from entry", ""],
        ["Tier 2 Stop Loss", "-30%", "from entry (optional)", ""],
        ["Maximum Portfolio Drawdown Alert", "-20%", "", ""],
    ]
    return data

def create_tier1_template():
    """Create Tier 1 (Core) scorecard template"""
    headers = [
        ["TIER 1 (CORE) - STOCK SCORECARD", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Target Allocation: 45% | Max Position: 15% | Focus: Quality & Stability", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["STOCK INFO", "", "", "", "VALUATION (20%)", "", "", "", "QUALITY (30%)", "", "", "", "GROWTH (30%)", "", "", ""],
        ["Symbol", "Company", "Price", "Mkt Cap ($B)", "P/E Score", "FCF Yield Score", "PEG Score", "Val Total", "ROIC Score", "Margin Score", "Moat Score", "Qual Total", "Rev Growth Score", "EPS Growth Score", "Growth Total", ""],
    ]

    # Add column headers for remaining sections
    headers.append([
        "Symbol", "Company", "Price", "Mkt Cap",
        "P/E (0-100)", "FCF Yield (0-100)", "PEG (0-100)", "Valuation Avg",
        "ROIC (0-100)", "Op Margin (0-100)", "Moat (0-100)", "Quality Avg",
        "Revenue Growth (0-100)", "EPS Growth (0-100)", "Growth Avg",
        "12M Return (0-100)", "Rel Strength (0-100)", "Technical (0-100)", "Momentum Avg",
        "Net Cash (0-100)", "FCF Gen (0-100)", "Fin Health Avg",
        "COMPOSITE SCORE", "RATING", "TARGET %", "CURRENT %", "ACTION", "NOTES"
    ])

    # Add example: GOOGL
    headers.append([
        "GOOGL", "Alphabet Inc", "$140", "1800",
        "85", "70", "60", "=AVERAGE(E7:G7)",
        "100", "100", "100", "=AVERAGE(I7:K7)",
        "55", "70", "=AVERAGE(M7:N7)",
        "80", "75", "100", "=AVERAGE(P7:R7)",
        "100", "100", "=AVERAGE(T7:U7)",
        "=E7*0.20+I7*0.30+M7*0.30+P7*0.10+T7*0.10",
        "=IF(W7>=85,\"Strong Buy\",IF(W7>=75,\"Buy\",IF(W7>=65,\"Hold\",IF(W7>=50,\"Reduce\",\"Sell\"))))",
        "12%", "11%", "=IF(W7>=75,\"Add/Hold\",IF(W7>=65,\"Monitor\",\"Trim\"))",
        "Network effects + scale moat"
    ])

    # Add empty rows for user input
    for i in range(10):
        headers.append(["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])

    return headers

def create_tier2_template():
    """Create Tier 2 (Emerging) scorecard template"""
    headers = [
        ["TIER 2 (EMERGING) - STOCK SCORECARD", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Target Allocation: 30% | Max Position: 8% | Focus: High Growth with Emerging Moats", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Symbol", "Company", "Price", "Mkt Cap ($B)",
         "P/S Score (0-100)", "PEG Score (0-100)", "Valuation Avg",
         "Scale Score (0-100)", "Gross Margin (0-100)", "NRR Score (0-100)", "Quality Avg",
         "Rev Growth (0-100)", "Growth Accel (0-100)", "TAM Score (0-100)", "Growth Avg",
         "6M Return (0-100)", "Rel Strength (0-100)", "Momentum Avg",
         "Moat Dev (0-100)", "Op Leverage (0-100)", "Scale/Moat Avg",
         "COMPOSITE SCORE", "RATING", "TARGET %", "CURRENT %", "ACTION", "NOTES"
        ]
    ]

    # Add example: PLTR
    headers.append([
        "PLTR", "Palantir", "$28", "65",
        "60", "75", "=AVERAGE(E6:F6)",
        "85", "100", "95", "=AVERAGE(H6:J6)",
        "90", "85", "100", "=AVERAGE(L6:N6)",
        "85", "100", "=AVERAGE(P6:Q6)",
        "100", "100", "=AVERAGE(S6:T6)",
        "=E6*0.18+H6*0.25+L6*0.35+P6*0.15+S6*0.07",
        "=IF(V6>=85,\"Strong Buy\",IF(V6>=75,\"Buy\",IF(V6>=65,\"Hold\",IF(V6>=50,\"Reduce\",\"Sell\"))))",
        "6%", "5.8%", "=IF(V6>=75,\"Add/Hold\",IF(V6>=65,\"Monitor\",\"Trim\"))",
        "Gov contracts + cloud partnerships"
    ])

    # Add empty rows
    for i in range(10):
        headers.append(["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])

    return headers

def create_tier3_template():
    """Create Tier 3 (Moonshots) scorecard template"""
    headers = [
        ["TIER 3 (MOONSHOTS) - STOCK SCORECARD", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Target Allocation: 20% | Max Position: 3% | Focus: Explosive Growth & Disruption | STOP LOSS: -40%", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["", "", "", "", "", "", "", "", "", "", "", "", "", ""],
        ["Symbol", "Company", "Price", "Mkt Cap ($B)", "Entry Price", "Stop Loss (-40%)",
         "P/S Score (0-100)", "Valuation Avg",
         "Gross Margin (0-100)", "Path to Profit (0-100)", "Quality Avg",
         "Rev Growth (0-100)", "TAM Score (0-100)", "Growth Accel (0-100)", "Growth Avg",
         "6M Return (0-100)", "Volume (0-100)", "Momentum Avg",
         "Market Disrupt (0-100)", "Tech Moat (0-100)", "Disruption Avg",
         "COMPOSITE SCORE", "RATING", "TARGET %", "CURRENT %", "ACTION", "NOTES"
        ]
    ]

    # Add example: RKLB
    headers.append([
        "RKLB", "Rocket Lab", "$9.50", "4.5", "$8.20", "=E6*0.6",
        "70", "70",
        "85", "80", "=AVERAGE(I6:J6)",
        "95", "100", "85", "=AVERAGE(L6:N6)",
        "100", "100", "=AVERAGE(P6:Q6)",
        "95", "90", "=AVERAGE(S6:T6)",
        "=G6*0.10+I6*0.15+L6*0.45+P6*0.20+S6*0.10",
        "=IF(V6>=85,\"Strong Buy\",IF(V6>=75,\"Buy\",IF(V6>=65,\"Hold\",IF(V6>=50,\"Reduce\",\"Sell\"))))",
        "2.5%", "2.1%",
        "=IF(C6<=F6,\"STOP LOSS HIT\",IF(V6>=75,\"Add/Hold\",IF(V6>=65,\"Monitor\",\"Trim\")))",
        "Creating cheap space access market"
    ])

    # Add empty rows
    for i in range(10):
        headers.append(["", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", ""])

    return headers

def create_dashboard():
    """Create Dashboard summary"""
    data = [
        ["PORTFOLIO DASHBOARD - 3-TIER STOCK RATING SYSTEM", "", "", "", "", ""],
        ["Last Updated: [DATE]", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["PORTFOLIO SUMMARY", "", "", "", "", ""],
        ["Total Portfolio Value", "$[ENTER VALUE]", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["Tier", "Target %", "Current %", "Current Value", "Variance", "Action"],
        ["Tier 1 (Core)", "45%", "=[SUM TIER1]", "=B8*$B$5", "=C8-B8", "=IF(ABS(E8)>0.05,\"Rebalance\",\"OK\")"],
        ["Tier 2 (Emerging)", "30%", "=[SUM TIER2]", "=B9*$B$5", "=C9-B9", "=IF(ABS(E9)>0.05,\"Rebalance\",\"OK\")"],
        ["Tier 3 (Moonshots)", "20%", "=[SUM TIER3]", "=B10*$B$5", "=C10-B10", "=IF(ABS(E10)>0.05,\"Rebalance\",\"OK\")"],
        ["Cash", "5%", "=[CALC]", "=B11*$B$5", "=C11-B11", ""],
        ["TOTAL", "100%", "=SUM(C8:C11)", "=SUM(D8:D11)", "", ""],
        ["", "", "", "", "", ""],
        ["PORTFOLIO METRICS", "", "", "", "", ""],
        ["Average Composite Score - Tier 1", "=[AVG]", "", "", "", ""],
        ["Average Composite Score - Tier 2", "=[AVG]", "", "", "", ""],
        ["Average Composite Score - Tier 3", "=[AVG]", "", "", "", ""],
        ["Overall Portfolio Score", "=[WEIGHTED AVG]", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["TOP HOLDINGS", "Symbol", "Tier", "Score", "Allocation %", "Rating"],
        ["1", "", "", "", "", ""],
        ["2", "", "", "", "", ""],
        ["3", "", "", "", "", ""],
        ["4", "", "", "", "", ""],
        ["5", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["ALERTS & ACTION ITEMS", "", "", "", "", ""],
        ["Stocks Below 65 Score (Review)", "[AUTO-POPULATE]", "", "", "", ""],
        ["Positions >10% Over Target (Trim)", "[AUTO-POPULATE]", "", "", "", ""],
        ["Tier 3 Stop Losses Hit", "[AUTO-POPULATE]", "", "", "", ""],
        ["Cash Deployment Opportunities (Score 80+)", "[AUTO-POPULATE]", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["PERFORMANCE TRACKING", "", "", "", "", ""],
        ["Month", "Portfolio Return %", "S&P 500 %", "QQQ %", "Relative Performance", "Notes"],
        ["Current Month", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["SCORING LEGEND", "", "", "", "", ""],
        ["85-100", "Strong Buy ⭐⭐⭐⭐⭐", "Actively add to position", "", "", ""],
        ["75-84", "Buy ⭐⭐⭐⭐", "Add or hold current position", "", "", ""],
        ["65-74", "Hold ⭐⭐⭐", "Monitor, no action needed", "", "", ""],
        ["50-64", "Reduce ⭐⭐", "Consider trimming position", "", "", ""],
        ["0-49", "Sell ⭐", "Exit position", "", "", ""],
    ]
    return data

def write_csv(filename, data):
    """Write data to CSV file"""
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def create_readme():
    """Create README with instructions"""
    return """# 3-Tier Stock Rating System Spreadsheet

## Quick Start Guide

### Files Included:
1. `config_weights.csv` - Configuration and weight settings
2. `tier1_core.csv` - Tier 1 (Core) stock scorecard
3. `tier2_emerging.csv` - Tier 2 (Emerging) stock scorecard
4. `tier3_moonshots.csv` - Tier 3 (Moonshots) stock scorecard
5. `dashboard.csv` - Portfolio dashboard and summary

### How to Use:

#### Option 1: Import into Excel
1. Open Microsoft Excel
2. Create a new workbook
3. For each CSV file:
   - Create a new sheet (Config, Tier 1, Tier 2, Tier 3, Dashboard)
   - Go to Data → From Text/CSV
   - Select the corresponding CSV file
   - Click "Load"
4. Review formulas (marked with = signs in CSV)
5. Set up cell formulas as indicated

#### Option 2: Import into Google Sheets
1. Open Google Sheets
2. File → Import
3. Upload tab → Select each CSV file
4. Import location: "Insert new sheet(s)"
5. Repeat for all CSV files
6. Rename sheets appropriately

### Setting Up Formulas:

The CSV files contain formula references like `=AVERAGE(E7:G7)`.

**In Excel/Google Sheets, you need to enter these formulas:**

#### Tier 1 (Core) Formulas:
- Column H (Valuation Total): `=AVERAGE(E7:G7)`
- Column L (Quality Total): `=AVERAGE(I7:K7)`
- Column O (Growth Total): `=AVERAGE(M7:N7)`
- Column S (Momentum Total): `=AVERAGE(P7:R7)`
- Column V (Financial Health Total): `=AVERAGE(T7:U7)`
- Column W (Composite Score): `=E7*0.20+I7*0.30+M7*0.30+P7*0.10+T7*0.10`
- Column X (Rating): `=IF(W7>=85,"Strong Buy",IF(W7>=75,"Buy",IF(W7>=65,"Hold",IF(W7>=50,"Reduce","Sell"))))`
- Column AA (Action): `=IF(W7>=75,"Add/Hold",IF(W7>=65,"Monitor","Trim"))`

Copy these formulas down for all rows.

#### Tier 2 (Emerging) Formulas:
- Adjust based on template structure
- Use weights: 18% Val, 25% Qual, 35% Growth, 15% Mom, 7% Scale/Moat

#### Tier 3 (Moonshots) Formulas:
- Add stop loss calculation: `=E6*0.6` (60% of entry price)
- Use weights: 10% Val, 15% Qual, 45% Growth, 20% Mom, 10% Disruption

### First Steps:

1. **Review Config & Weights tab**
   - Verify default weights match your strategy
   - Adjust if needed (ensure each tier totals 100%)

2. **Start with Tier 1**
   - Enter 3-5 of your largest holdings
   - Input scores for each component (0-100)
   - Watch composite score calculate automatically

3. **Use Example Stocks as Reference**
   - GOOGL (Tier 1)
   - PLTR (Tier 2)
   - RKLB (Tier 3)

4. **Check Dashboard**
   - Monitor overall portfolio allocation
   - Track alerts and action items

### Scoring Tips:

- **All component scores should be 0-100**
- Use the detailed scoring guide document for methodology
- Be honest and consistent with your scoring
- Update quarterly (minimum) or after major news

### Support:

Refer to the complete "3-Tier Stock Rating System - Complete Scoring Guide"
document for detailed scoring methodologies, examples, and FAQs.

### Version: 1.0
**Created:** October 2025
"""

def main():
    """Generate all spreadsheet files"""
    print("Generating 3-Tier Stock Rating System Spreadsheet...")

    # Create output directory
    output_dir = "stock_rating_spreadsheet"
    os.makedirs(output_dir, exist_ok=True)

    # Generate each CSV file
    print("Creating Config & Weights...")
    write_csv(f"{output_dir}/config_weights.csv", create_config_weights())

    print("Creating Tier 1 (Core) scorecard...")
    write_csv(f"{output_dir}/tier1_core.csv", create_tier1_template())

    print("Creating Tier 2 (Emerging) scorecard...")
    write_csv(f"{output_dir}/tier2_emerging.csv", create_tier2_template())

    print("Creating Tier 3 (Moonshots) scorecard...")
    write_csv(f"{output_dir}/tier3_moonshots.csv", create_tier3_template())

    print("Creating Dashboard...")
    write_csv(f"{output_dir}/dashboard.csv", create_dashboard())

    print("Creating README...")
    with open(f"{output_dir}/README.md", 'w') as f:
        f.write(create_readme())

    print(f"\n✓ Spreadsheet files created successfully in '{output_dir}/' directory!")
    print("\nFiles created:")
    print("  - config_weights.csv")
    print("  - tier1_core.csv")
    print("  - tier2_emerging.csv")
    print("  - tier3_moonshots.csv")
    print("  - dashboard.csv")
    print("  - README.md")
    print("\nNext steps:")
    print("1. Import CSV files into Excel or Google Sheets")
    print("2. Set up formulas as described in README.md")
    print("3. Start scoring your stocks!")

if __name__ == "__main__":
    main()
