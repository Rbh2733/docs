# 3-Tier Stock Rating System Spreadsheet

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
