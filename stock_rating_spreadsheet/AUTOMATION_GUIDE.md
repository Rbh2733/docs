# Stock Rating System - Automation Guide

## 🚀 Quick Start - 3 Levels of Automation

### Level 1: One-Click Manual Update (Easiest)
Run whenever you want to update your ratings:
```bash
python3 auto_stock_rater.py
```

### Level 2: Scheduled Daily Updates
Automatically update every day at market open:
```bash
python3 scheduler.py --mode daily --time "09:30"
```

### Level 3: Continuous Real-Time Monitoring
Update every 4 hours during market hours:
```bash
python3 scheduler.py --mode interval --hours 4
```

---

## 📋 Installation

### 1. Install Required Packages

```bash
pip install -r requirements.txt
```

This installs:
- `yfinance` - Free stock data from Yahoo Finance
- `pandas` - Data analysis
- `openpyxl` - Excel file generation
- `schedule` - Task scheduling
- Other supporting libraries

### 2. Verify Installation

```bash
python3 -c "import yfinance; print('✓ yfinance installed')"
python3 -c "import pandas; print('✓ pandas installed')"
```

---

## 🎯 What Gets Automated

### Automatic Data Fetching
- **Real-time prices** from Yahoo Finance
- **Financial metrics**: P/E, P/S, revenue growth, margins
- **Cash flow data**: FCF, cash position, debt
- **Price momentum**: 6-month and 12-month returns
- **Technical indicators**: 50-day and 200-day moving averages
- **Benchmark comparison**: Relative strength vs QQQ

### Automatic Scoring
- **All component scores calculated** (0-100 scale)
- **Weighted composite scores** for each tier
- **Automatic ratings** (Strong Buy ⭐⭐⭐⭐⭐ to Sell ⭐)
- **Position sizing recommendations**

### Automatic Alerts
- 🌟 **Strong Buy opportunities** (score ≥ 85)
- ⚠️ **Review needed** (score < 65)
- 🛑 **Stop losses hit** (Tier 3 only)
- 📊 **Portfolio rebalancing** suggestions

---

## 📊 Usage Examples

### Basic Usage

#### 1. Update Your Watchlist

Edit `watchlist.json`:
```json
{
  "tier1": ["GOOGL", "AAPL", "MSFT", "NVDA"],
  "tier2": ["PLTR", "SNOW", "CRWD"],
  "tier3": ["RKLB", "IONQ", "HOOD"]
}
```

#### 2. Run One-Time Update

```bash
python3 auto_stock_rater.py
```

**Output:**
- Console display of all scores
- CSV files: `tier1_scores_YYYYMMDD_HHMMSS.csv`, etc.
- HTML dashboard: `dashboard.html`

#### 3. Open Dashboard

```bash
# On Mac
open dashboard.html

# On Linux
xdg-open dashboard.html

# On Windows
start dashboard.html
```

---

### Advanced Scheduling

#### Daily Updates at Market Open (9:30 AM ET)

```bash
python3 scheduler.py --mode daily --time "09:30"
```

Runs every weekday at 9:30 AM.

#### Weekly Updates (Monday Morning)

```bash
python3 scheduler.py --mode weekly --day monday --time "09:00"
```

#### Interval Updates (Every 4 Hours)

```bash
python3 scheduler.py --mode interval --hours 4
```

Useful for active traders.

#### One-Time Update Only

```bash
python3 scheduler.py --mode once
```

---

## 📈 Understanding the Output

### Console Output

```
================================================================================
AUTOMATED STOCK RATING - 2025-10-23 09:30:00
================================================================================

TIER 1 (CORE) STOCKS:
--------------------------------------------------------------------------------
GOOGL  $ 140.50  Score:  82.4  Buy ⭐⭐⭐⭐
AAPL   $ 178.25  Score:  79.1  Buy ⭐⭐⭐⭐
MSFT   $ 372.15  Score:  85.3  Strong Buy ⭐⭐⭐⭐⭐

================================================================================
PORTFOLIO SUMMARY
================================================================================

Total stocks rated: 15
  Tier 1 (Core): 5
  Tier 2 (Emerging): 5
  Tier 3 (Moonshots): 5

Average Tier 1 Score: 81.2
Average Tier 2 Score: 76.8
Average Tier 3 Score: 72.5

================================================================================
ALERTS & ACTION ITEMS
================================================================================
⭐ Tier 1 STRONG BUY: MSFT - Score: 85.3
⭐ Tier 2 STRONG BUY: PLTR - Score: 86.4
⚠️  Tier 3 REVIEW: COIN - Score: 58.2 (Reduce ⭐⭐)
```

### CSV Output Files

**Location:** Current directory

**Files:**
- `tier1_scores_20251023_093000.csv`
- `tier2_scores_20251023_093000.csv`
- `tier3_scores_20251023_093000.csv`

**Columns:**
```csv
symbol,price,market_cap,valuation_score,quality_score,growth_score,
momentum_score,financial_health_score,composite_score,rating,
forward_pe,peg_ratio,revenue_growth,operating_margins,free_cash_flow
```

### HTML Dashboard

**Location:** `dashboard.html`

**Features:**
- 📊 Visual score cards with progress bars
- 📈 Sortable tables for each tier
- ⚡ Highlighted alerts and action items
- 🎨 Color-coded scores (green=excellent, red=poor)
- 📱 Mobile-responsive design

---

## 🔧 Customization

### Adjust Scoring Weights

Edit `auto_stock_rater.py`:

```python
# In Tier1Scorer.calculate_composite_score()

# Current weights:
composite = (valuation_avg * 0.20 +
            quality_avg * 0.30 +
            growth_avg * 0.30 +
            momentum_avg * 0.10 +
            financial_health_avg * 0.10)

# Example: Increase growth weight
composite = (valuation_avg * 0.15 +
            quality_avg * 0.25 +
            growth_avg * 0.40 +  # Changed!
            momentum_avg * 0.10 +
            financial_health_avg * 0.10)
```

### Adjust Rating Thresholds

```python
# Current thresholds:
if composite >= 85:
    rating = "Strong Buy ⭐⭐⭐⭐⭐"
elif composite >= 75:
    rating = "Buy ⭐⭐⭐⭐"
elif composite >= 65:
    rating = "Hold ⭐⭐⭐"

# Make more conservative:
if composite >= 90:  # Stricter!
    rating = "Strong Buy ⭐⭐⭐⭐⭐"
```

### Add Custom Metrics

```python
# In StockDataFetcher.get_stock_data()

# Add any metric from yfinance info dict:
data['dividend_yield'] = info.get('dividendYield', 0)
data['earnings_date'] = info.get('earningsDate', None)
data['analyst_rating'] = info.get('recommendationKey', 'none')
```

---

## 🔔 Setting Up Alerts

### Email Alerts (Coming Soon)

Future feature: Get email notifications when:
- Strong Buy opportunities appear (score ≥ 85)
- Holdings drop below Hold threshold (score < 65)
- Tier 3 stop losses are hit

### Slack/Discord Webhooks (Advanced)

Add to `auto_stock_rater.py`:

```python
import requests

def send_alert(message: str):
    webhook_url = "YOUR_WEBHOOK_URL"
    requests.post(webhook_url, json={"text": message})

# In generate_alerts():
for alert in alerts:
    send_alert(alert)
```

---

## 📅 Recommended Schedules

### Conservative Long-Term Investor
```bash
python3 scheduler.py --mode weekly --day sunday --time "20:00"
```
- Update once per week
- Review on Sunday evening
- Make trades Monday morning

### Active Trader
```bash
python3 scheduler.py --mode daily --time "09:30"
```
- Update daily at market open
- Review pre-market
- Adjust positions intraday

### Day Trader / Swing Trader
```bash
python3 scheduler.py --mode interval --hours 2
```
- Update every 2 hours
- Real-time monitoring
- Quick reaction to changes

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'yfinance'"

**Solution:**
```bash
pip install yfinance pandas numpy openpyxl
```

### "No data found for symbol XXX"

**Causes:**
- Ticker symbol changed or delisted
- Yahoo Finance API temporary outage
- Invalid ticker symbol

**Solution:**
- Verify ticker on Yahoo Finance website
- Remove or update symbol in `watchlist.json`

### "Rate limit exceeded"

**Cause:** Too many API requests to Yahoo Finance

**Solution:**
- Add delays between stocks:
```python
import time
time.sleep(1)  # Wait 1 second between requests
```

### Scores seem inaccurate

**Possible causes:**
1. **Missing data**: Some metrics not available for stock
2. **Extreme values**: Very high/low metrics skewing scores
3. **Sector differences**: Tech vs retail have different norms

**Solution:**
- Check raw data in CSV output
- Adjust scoring thresholds for your portfolio style
- Add sector-specific scoring (advanced)

---

## 🎓 Best Practices

### 1. Start Small
- Begin with 5-10 stocks you know well
- Verify automated scores match your manual analysis
- Gradually add more stocks

### 2. Review Regularly
- Don't blindly follow automated ratings
- Use scores as a starting point for research
- Add notes/context in spreadsheet

### 3. Customize for Your Style
- Adjust weights to match your investment philosophy
- Value investor? Increase valuation weight
- Growth investor? Increase growth weight

### 4. Track Performance
- Export historical CSV files
- Compare scores to actual returns
- Refine scoring over time

### 5. Combine with Manual Research
- Read earnings calls
- Understand business fundamentals
- Use automation to save time, not replace thinking

---

## 📊 Data Limitations

### What yfinance Provides (FREE ✓)
- Real-time prices (15-min delay)
- Financial statements (quarterly/annual)
- Key metrics (P/E, margins, etc.)
- Historical prices
- Basic company info

### What It Doesn't Provide
- ❌ Net Revenue Retention (NRR) - requires manual input
- ❌ Total Addressable Market (TAM) - requires research
- ❌ Competitive moat assessment - requires analysis
- ❌ Management quality - requires judgment
- ❌ Industry-specific metrics

### Manual Inputs Needed
For best results, manually add:
- NRR for SaaS companies (from earnings calls)
- TAM estimates (from company presentations)
- Moat assessment (your analysis)
- Industry context

---

## 🚀 Next Steps

### Week 1: Setup
- [ ] Install requirements
- [ ] Create your watchlist
- [ ] Run first automated update
- [ ] Review HTML dashboard

### Week 2: Validation
- [ ] Compare automated scores to your manual analysis
- [ ] Adjust weights if needed
- [ ] Test different stocks

### Week 3: Automation
- [ ] Set up daily/weekly scheduler
- [ ] Create backup routine for CSV files
- [ ] Set up alert notifications

### Month 2+: Optimization
- [ ] Track score changes over time
- [ ] Correlate scores with returns
- [ ] Fine-tune scoring algorithms
- [ ] Add custom metrics

---

## 💡 Pro Tips

### 1. Version Control Your Watchlist
```bash
git add watchlist.json
git commit -m "Added NVDA to Tier 1"
```

### 2. Archive Historical Scores
```bash
mkdir archives
mv tier*_scores_*.csv archives/
```

### 3. Run Pre-Market
Set scheduler for 9:00 AM to review before market opens at 9:30 AM.

### 4. Combine with Screeners
Use automated ratings on stocks from screeners:
```python
# Add stocks from Finviz screener to watchlist
watchlist['tier2'].extend(['NEW1', 'NEW2', 'NEW3'])
```

### 5. Create Comparison Reports
```bash
# Run on multiple dates, then compare
diff tier1_scores_20251020.csv tier1_scores_20251023.csv
```

---

## 🔮 Future Enhancements

**Coming soon:**
- [ ] Excel file generation (not just CSV)
- [ ] Email alert system
- [ ] Web-based configuration UI
- [ ] Cloud hosting option
- [ ] Portfolio performance tracking
- [ ] Sector rotation analysis
- [ ] AI-powered insights

---

## 📚 Additional Resources

### Learning More
- **yfinance docs**: https://github.com/ranaroussi/yfinance
- **Pandas docs**: https://pandas.pydata.org/docs/
- **Python scheduling**: https://schedule.readthedocs.io/

### Community
- Share your customizations
- Report bugs
- Request features

---

## ⚠️ Disclaimer

**This automation system is for informational purposes only.**

- Not financial advice
- Do your own research
- Past performance ≠ future results
- Markets are unpredictable
- Automated scores are starting points, not decisions

**Always:**
- Understand what you're buying
- Know your risk tolerance
- Diversify appropriately
- Consult financial professionals

---

**Happy Automating! 🤖📈**

Version 1.0 | Created October 2025
