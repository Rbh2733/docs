# 3-Tier Stock Rating System

## 🚀 NEW: Fully Automated System!

**The system now includes complete automation with real-time data fetching and automatic scoring!**

### Two Ways to Use This System:

#### Option 1: AUTOMATED (Recommended ⭐)
- **Real-time data** from Yahoo Finance
- **Automatic scoring** of all metrics
- **One-click updates** - just run a script
- **HTML dashboard** with visualizations
- **Scheduled updates** (daily, weekly, or custom)
- **Alerts** for buy/sell signals

👉 **[Read the AUTOMATION_GUIDE.md](AUTOMATION_GUIDE.md)** to get started!

**Quick Start (Automated):**
```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Edit your watchlist
nano watchlist.json

# 3. Run the automation
python3 auto_stock_rater.py

# 4. Open the dashboard
open dashboard.html
```

Or use the one-click script:
```bash
./quick_start.sh
```

#### Option 2: Manual Spreadsheet
- Import CSV files into Excel/Google Sheets
- Manually enter data and scores
- Good for learning the methodology
- Full control over every input

---

## 📦 Files Included

### Automation Files (NEW!):
1. **`auto_stock_rater.py`** - Main automation script (fetches data, calculates scores)
2. **`dashboard_generator.py`** - Generates beautiful HTML dashboards
3. **`scheduler.py`** - Schedule automatic daily/weekly updates
4. **`watchlist.json`** - Configure which stocks to track
5. **`requirements.txt`** - Python package dependencies
6. **`AUTOMATION_GUIDE.md`** - Complete automation documentation (START HERE!)
7. **`quick_start.sh`** - One-click setup and run script

### Spreadsheet Files (Original):
1. `config_weights.csv` - Configuration and weight settings
2. `tier1_core.csv` - Tier 1 (Core) stock scorecard
3. `tier2_emerging.csv` - Tier 2 (Emerging) stock scorecard
4. `tier3_moonshots.csv` - Tier 3 (Moonshots) stock scorecard
5. `dashboard.csv` - Portfolio dashboard and summary

### Documentation:
1. **`AUTOMATION_GUIDE.md`** - How to use the automated system ⭐ START HERE!
2. **`SCORING_GUIDE.md`** - Complete scoring methodology and examples
3. `README.md` - This file
4. `stock_rating_system.py` - Original CSV generator script

---

## 🎯 What Does Automation Do?

### Automatically Fetches:
- Real-time stock prices
- P/E ratios, P/S ratios, PEG ratios
- Revenue growth, earnings growth
- Operating margins, gross margins
- Free cash flow, cash position, debt
- 6-month and 12-month price returns
- Relative strength vs QQQ benchmark
- 50-day and 200-day moving averages

### Automatically Calculates:
- All component scores (0-100 scale)
- Weighted composite scores for each tier
- Buy/Sell/Hold ratings
- Stop loss prices (Tier 3)

### Automatically Generates:
- CSV files with all data and scores
- Interactive HTML dashboard
- Alerts for strong buy opportunities
- Warnings for stocks below thresholds
- Stop loss alerts for Tier 3

---

## 🚀 Quick Start - Automated System

### 1. Install Requirements

```bash
pip install -r requirements.txt
```

Installs: yfinance, pandas, numpy, openpyxl, schedule

### 2. Configure Your Watchlist

Edit `watchlist.json`:
```json
{
  "tier1": ["GOOGL", "AAPL", "MSFT", "NVDA", "META"],
  "tier2": ["PLTR", "SNOW", "DDOG", "CRWD", "NET"],
  "tier3": ["RKLB", "IONQ", "HOOD", "SOFI", "COIN"]
}
```

### 3. Run the Automation

```bash
python3 auto_stock_rater.py
```

### 4. View Results

- **HTML Dashboard**: Open `dashboard.html` in your browser
- **CSV Files**: `tier1_scores_YYYYMMDD_HHMMSS.csv` (import to Excel)
- **Console Output**: See scores and alerts immediately

### 5. Set Up Automatic Updates (Optional)

**Daily at market open (9:30 AM):**
```bash
python3 scheduler.py --mode daily --time "09:30"
```

**Weekly on Monday:**
```bash
python3 scheduler.py --mode weekly --day monday --time "09:00"
```

**Every 4 hours:**
```bash
python3 scheduler.py --mode interval --hours 4
```

---

## 📊 Manual Spreadsheet Usage

### How to Use CSV Files:

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

---

## 📚 Documentation

### For Automation Users:
1. **[AUTOMATION_GUIDE.md](AUTOMATION_GUIDE.md)** - Complete guide to automated system
   - Installation instructions
   - Usage examples
   - Scheduling options
   - Customization guide
   - Troubleshooting

### For All Users:
2. **[SCORING_GUIDE.md](SCORING_GUIDE.md)** - Detailed scoring methodology
   - How each metric is scored (0-100)
   - Example calculations
   - Data sources
   - FAQ

---

## 🎯 System Overview

### The 3-Tier System:

**Tier 1 (Core) - 45% of Portfolio**
- Large-cap, established companies
- Focus: Quality + Stability
- Max position: 15%
- Weights: Valuation 20%, Quality 30%, Growth 30%, Momentum 10%, Fin Health 10%

**Tier 2 (Emerging) - 30% of Portfolio**
- High-growth companies with developing moats
- Focus: Revenue Growth
- Max position: 8%
- Weights: Valuation 18%, Quality 25%, Growth 35%, Momentum 15%, Moat 7%

**Tier 3 (Moonshots) - 20% of Portfolio**
- Speculative, high-risk/high-reward
- Focus: Disruption Potential
- Max position: 3%
- **Mandatory stop loss: -40%**
- Weights: Valuation 10%, Quality 15%, Growth 45%, Momentum 20%, Disruption 10%

**Cash - 5%**
- Dry powder for opportunities

---

## 🔔 Key Features

### Automated System Features:
✅ Real-time data from Yahoo Finance (free!)
✅ Automatic calculation of all scores
✅ HTML dashboard with visualizations
✅ CSV export for Excel analysis
✅ Alert system for buy/sell signals
✅ Scheduled daily/weekly updates
✅ Stop loss monitoring (Tier 3)
✅ Relative strength vs QQQ
✅ Technical indicator tracking

### Manual System Features:
✅ Complete control over inputs
✅ Excel/Google Sheets compatible
✅ Example stocks (GOOGL, PLTR, RKLB)
✅ Pre-configured formulas
✅ Portfolio dashboard template

---

## 💡 Best Practices

### For Automated Users:
1. **Start small** - Test with 5-10 stocks first
2. **Verify scores** - Compare automated scores to your manual analysis
3. **Customize weights** - Adjust to match your investment style
4. **Update regularly** - Daily for active traders, weekly for long-term
5. **Don't blindly follow** - Use scores as starting point for research

### For Manual Users:
1. **Be consistent** - Use same data sources every time
2. **Update quarterly** - After earnings releases
3. **Document reasoning** - Use Notes column
4. **Track changes** - Monitor score trends over time

---

## 🛠️ Customization

Both systems are highly customizable:

- **Adjust scoring weights** to match your strategy
- **Change rating thresholds** (more/less conservative)
- **Add custom metrics** from yfinance
- **Modify tier allocations** (e.g., 50% Core, 25% Emerging, 25% Moonshots)
- **Set custom alerts** (email, Slack, Discord)

See AUTOMATION_GUIDE.md for detailed customization instructions.

---

## 📈 Example Output

### Automated Console Output:
```
================================================================================
TIER 1 (CORE) STOCKS:
--------------------------------------------------------------------------------
GOOGL  $ 140.50  Score:  82.4  Buy ⭐⭐⭐⭐
MSFT   $ 372.15  Score:  85.3  Strong Buy ⭐⭐⭐⭐⭐
NVDA   $ 495.20  Score:  88.7  Strong Buy ⭐⭐⭐⭐⭐

================================================================================
ALERTS & ACTION ITEMS
================================================================================
⭐ Tier 1 STRONG BUY: MSFT - Score: 85.3
⭐ Tier 1 STRONG BUY: NVDA - Score: 88.7
⚠️  Tier 3 REVIEW: COIN - Score: 58.2 (Reduce ⭐⭐)
```

### HTML Dashboard:
Beautiful, interactive dashboard with:
- Color-coded score cards
- Sortable tables
- Visual progress bars
- Alert highlights
- Mobile-responsive design

---

## 🐛 Troubleshooting

### Automation Issues:

**"ModuleNotFoundError: No module named 'yfinance'"**
```bash
pip install yfinance pandas numpy openpyxl
```

**"No data found for symbol XXX"**
- Verify ticker symbol is correct
- Check if stock is still trading
- Remove from watchlist.json if delisted

**Scores seem wrong**
- Check raw data in CSV output
- Verify ticker symbols
- Some metrics may not be available for all stocks

See AUTOMATION_GUIDE.md for complete troubleshooting guide.

---

## 📖 Learning Path

### Week 1: Get Started
1. Run automated system with default watchlist
2. Review HTML dashboard
3. Compare scores to your own analysis
4. Read SCORING_GUIDE.md to understand methodology

### Week 2: Customize
1. Edit watchlist.json with your stocks
2. Adjust scoring weights if needed
3. Set up daily/weekly scheduler

### Week 3: Optimize
1. Track score changes over time
2. Correlate scores with actual returns
3. Fine-tune your approach

---

## ⚠️ Important Notes

### Data Limitations:
- **yfinance provides most data** but not everything
- **Some metrics require manual input**: NRR, TAM, moat assessment
- **15-minute price delay** (not real-time tick data)
- **Fundamentals updated quarterly** (after earnings)

### Disclaimer:
This system is for **informational and educational purposes only**.

- Not financial advice
- Do your own research
- Understand your risk tolerance
- Markets are unpredictable
- Past performance ≠ future results

**Always consult financial professionals before making investment decisions.**

---

## 🚀 Next Steps

### Choose Your Path:

**Path A: Automated System (Recommended)**
1. Read [AUTOMATION_GUIDE.md](AUTOMATION_GUIDE.md)
2. Run `./quick_start.sh`
3. Edit `watchlist.json`
4. Review `dashboard.html`

**Path B: Manual Spreadsheet**
1. Import CSV files to Excel/Google Sheets
2. Read [SCORING_GUIDE.md](SCORING_GUIDE.md)
3. Enter your stocks
4. Start scoring

---

## 📧 Support & Community

- **Documentation**: Read AUTOMATION_GUIDE.md and SCORING_GUIDE.md
- **Issues**: Check troubleshooting sections
- **Customization**: Both guides include customization instructions

---

## 🎉 What's New in Version 1.1

✨ **Full automation with real-time data**
✨ **HTML dashboard with visualizations**
✨ **Scheduled daily/weekly updates**
✨ **Alert system for buy/sell signals**
✨ **One-click setup script**
✨ **Comprehensive automation guide**

---

**Happy Investing! 📈🚀**

**Version:** 1.1
**Created:** October 2025
**Last Updated:** October 2025
