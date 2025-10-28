# Single-Sheet Stock Rating System

A comprehensive, automated stock scoring system built for Google Sheets that evaluates stocks across three tiers using 25+ financial metrics.

## 🎯 What Is This?

This is a **streamlined, single-sheet stock rating system** that automatically:
- ✅ Classifies stocks into 3 tiers based on market cap
- ✅ Calculates 5 component scores (Valuation, Quality, Growth, Momentum, Financial Health)
- ✅ Generates a composite score (0-100) with star ratings
- ✅ Provides action signals (ADD, HOLD, EXIT, etc.)
- ✅ Uses tier-specific formulas optimized for each stock type

### The Three Tiers

| Tier | Market Cap | Examples | Investment Focus |
|------|-----------|----------|------------------|
| **Tier 1: Core** | >$300B | GOOGL, AMZN, NVDA, META, MSFT | Stability & consistent growth |
| **Tier 2: Emerging** | $20-150B | PLTR, MU, CRWD, SNOW, NET | Accelerated growth |
| **Tier 3: Moonshots** | <$20B | RKLB, IONQ, COIN, HOOD | Asymmetric upside potential |

---

## 📁 Files in This Package

### 1. **QUICK_START_IMPORT.md** ⚡ START HERE
**5-minute setup guide** - Import pre-built template with formulas

### 2. **stock_rating_template.csv** 📊
**Ready-to-import template** with:
- All formulas pre-configured
- 3 example stocks (GOOGL, PLTR, RKLB)
- Headers and structure ready

### 3. **GOOGLE_SHEETS_IMPLEMENTATION.md** 🔧
**Complete technical guide** with:
- Every formula explained
- Step-by-step manual setup
- Conditional formatting instructions
- Troubleshooting tips

### 4. **SINGLE_SHEET_STOCK_RATING_USER_GUIDE.md** 📖
**Comprehensive user manual** covering:
- How the scoring system works
- Where to find each metric
- Portfolio management strategies
- Risk management rules
- Real-world examples

### 5. **Python_Script_for_Historical_Stock_Data.ipynb** 🐍
**Jupyter notebook** for automating data collection (optional)

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Import the Template
1. Download `stock_rating_template.csv`
2. Go to [Google Sheets](https://sheets.google.com)
3. **File → Import → Upload**
4. **Important:** Enable "Convert text to numbers, dates, and formulas"
5. Click Import

### Step 2: Verify It Works
Check that:
- Cell E2 shows "Tier 1" (not formula text)
- Cells AA2-AH2 show numbers and text (not formulas as text)
- GOOGL, PLTR, RKLB examples are visible with scores

### Step 3: Apply Basic Formatting
1. Make Row 1 **bold** and **gray background**
2. Color columns A-D, F-Z **blue** (these are inputs)
3. Color columns E, AA-AH **black/bold** (these are calculated)

### Step 4: Add Your First Stock
1. Pick a stock you own (e.g., NVDA)
2. Gather data from Yahoo Finance, Seeking Alpha
3. Enter in Row 5 (or replace examples)
4. Watch it auto-calculate!

**Full details:** See `QUICK_START_IMPORT.md`

---

## 📊 How It Works

### The Scoring Formula

```
INPUT DATA (25 metrics)
    ↓
AUTOMATIC TIER CLASSIFICATION (based on market cap)
    ↓
COMPONENT SCORES (5 scores, tier-specific formulas)
    ↓
COMPOSITE SCORE (weighted average by tier)
    ↓
RATING (★★★★★ to ★) + ACTION SIGNAL
```

### What You Enter (Input Columns)

**Basic Info:** Ticker, Company, Price, Market Cap, Beta, Sector

**Valuation:** Forward P/E, 5yr Avg P/E, FCF, P/S Ratio

**Growth:** Revenue Growth %, EPS Growth %

**Quality:** Operating Margin %, ROIC %, Gross Margin %, NRR %, Moat

**Momentum:** 12-month Return %, Above 200-day MA?

**Health:** Net Cash, Insider Ownership %, Cash Conversion

### What Gets Calculated (Auto-Calculated)

**Component Scores (0-100 each):**
- Valuation Score
- Quality Score
- Growth Score
- Momentum Score
- Financial Health Score

**Final Output:**
- **Composite Score** (0-100 weighted average)
- **Rating** (★★★★★ Strong Buy to ★ Exit/Pass)
- **Action** (ADD, HOLD, REDUCE, EXIT, etc.)

---

## 🎨 Tier-Specific Weighting

Each tier uses different weights because different stocks require different focus:

### Tier 1: Core Holdings (>$300B)
- **Quality:** 30% - Established leaders should have strong fundamentals
- **Growth:** 30% - Consistent, sustainable growth
- **Valuation:** 20% - Price matters, but quality comes first
- **Momentum:** 10% - Less critical for long-term holds
- **Health:** 10% - These companies are typically stable

**Rating Thresholds:**
- 85+: ★★★★★ Strong Buy
- 75-84: ★★★★ Buy
- 65-74: ★★★ Hold
- 55-64: ★★ Reduce
- <55: ★ Exit

### Tier 2: Emerging Leaders ($20-150B)
- **Growth:** 35% - Growth is the primary driver
- **Quality:** 25% - Need solid fundamentals
- **Valuation:** 18% - Can pay for growth
- **Momentum:** 12% - Technical strength matters
- **Health:** 10% - Cash flow becoming important

**Rating Thresholds:**
- 85+: ★★★★★ Strong Buy
- 75-84: ★★★★ Buy
- 65-74: ★★★ Accumulate
- 55-64: ★★ Hold
- <55: ★ Exit

### Tier 3: Moonshots (<$20B)
- **Growth:** 45% - Hypergrowth is everything
- **Momentum:** 20% - Narrative and sentiment critical
- **Quality:** 15% - Nice to have, not required
- **Valuation:** 15% - Willing to pay for potential
- **Health:** 5% - Can burn cash if growing

**Rating Thresholds:**
- 80+: ★★★★★ Strong Buy
- 70-79: ★★★★ Buy
- 65-69: ★★★ Speculative Buy
- 60-64: ★★ Watch
- <60: ★ Pass

---

## 📈 Example Scores

### GOOGL (Tier 1 - Core)
- Market Cap: $1,800B
- Valuation: 65 (reasonable P/E vs historical)
- Quality: 88 (excellent margins, moat)
- Growth: 78 (solid 13% revenue growth)
- Momentum: 85 (strong 45% return)
- Health: 95 ($100B net cash)
- **Composite: 82 → ★★★★ Buy → Action: ADD**

### PLTR (Tier 2 - Emerging)
- Market Cap: $60B
- Valuation: 55 (high P/E but justified)
- Quality: 82 (improving margins, high NRR)
- Growth: 95 (30% revenue growth)
- Momentum: 90 (68% return, strong trend)
- Health: 75 (positive cash flow)
- **Composite: 86 → ★★★★★ Strong Buy → Action: ADD**

### RKLB (Tier 3 - Moonshot)
- Market Cap: $6B
- Valuation: 48 (high P/S for unprofitable)
- Quality: 65 (good gross margin despite losses)
- Growth: 100 (85% revenue growth, huge TAM)
- Momentum: 95 (110% return, massive momentum)
- Health: 45 (burning cash, but expected)
- **Composite: 78 → ★★★★ Buy → Action: ADD**

---

## 🗂️ Data Sources

### Free Resources (No Account Needed)

**Yahoo Finance** - Price, Market Cap, Beta, P/E, P/S
- https://finance.yahoo.com

**Seeking Alpha** - Growth rates, Margins, Financials
- https://seekingalpha.com

**Macrotrends** - Historical P/E averages
- https://macrotrends.net

**GuruFocus** - ROIC, Quality metrics
- https://gurufocus.com

**SEC EDGAR** - 10-K, 10-Q filings (raw data)
- https://sec.gov/edgar

**Company IR Sites** - TAM data, strategic presentations

**TradingView** - Charts, 200-day MA checks
- https://tradingview.com

---

## 💼 Portfolio Management

### Recommended Allocation

| Tier | Portfolio % | # of Stocks | Position Size |
|------|------------|-------------|---------------|
| **Tier 1** | 40-50% | 4-6 stocks | 8-12% each |
| **Tier 2** | 25-35% | 4-7 stocks | 4-8% each |
| **Tier 3** | 20-30% | 8-12 stocks | 2-4% each |
| **Cash** | 5-10% | - | Buffer |

### Position Sizing by Score

**High conviction (85+ score):** Upper end of range
**Medium conviction (75-84):** Middle of range
**Lower conviction (65-74):** Lower end or watch list

### Risk Management

**Tier 1:** No hard stop loss, exit if score <65 for 2 quarters
**Tier 2:** Stop loss at -35% or score <55
**Tier 3:** **HARD STOP at -40%** or score <50 (non-negotiable!)

---

## 🔄 Maintenance Schedule

### Weekly (15 minutes)
- Update prices (column C)
- Update 12-month returns (column V)
- Check 200-day MA status (column W)
- Review action signals

### Monthly (1-2 hours)
- Full re-score after earnings
- Update growth rates and margins
- Rebalance positions >2% off target

### Quarterly (2-3 hours)
- Complete data refresh
- Assess tier migrations
- Major rebalancing decisions
- Review and refine process

---

## 🛠️ Customization

The system is designed to be customizable. You can:

1. **Adjust tier thresholds** - Change the $300B and $20B cutoffs
2. **Modify component weights** - Change the importance of each score
3. **Add new metrics** - Insert columns for additional data points
4. **Change rating thresholds** - Adjust when stocks get 5 stars vs 4 stars
5. **Customize action signals** - Define your own buy/sell triggers

**Important:** Document any changes you make and test thoroughly!

---

## 📚 Learning Resources

### Start Here
1. **QUICK_START_IMPORT.md** - Get up and running (5 min)
2. **SINGLE_SHEET_STOCK_RATING_USER_GUIDE.md** - Learn the system (30 min)
3. **GOOGLE_SHEETS_IMPLEMENTATION.md** - Understand the formulas (as needed)

### Deep Dives
- **User Guide Section: "Understanding the Scoring Formulas"** - How each component is calculated
- **User Guide Section: "Position Sizing & Portfolio Management"** - How to use the scores
- **User Guide Section: "Risk Management"** - When to exit positions

### Practice
1. Score 2-3 stocks you already know well
2. Compare scores to your intuition
3. Adjust understanding as needed
4. Build confidence before using for real decisions

---

## ⚠️ Important Disclaimers

### This Is A Tool, Not Advice
- **Not financial advice** - Do your own research
- **Not a guarantee** - Past performance doesn't predict future results
- **Not automated trading** - Requires human judgment
- **Not a replacement for due diligence** - Still read 10-Ks, listen to earnings calls

### Limitations
- **Garbage in, garbage out** - Accuracy depends on your data quality
- **Backward-looking** - Metrics are historical, market is forward-looking
- **Cannot predict** - Black swan events, management changes, etc.
- **Optimized for growth** - Not ideal for dividend/value investing

### Best Practices
- ✅ Use as one input among many
- ✅ Combine with qualitative research
- ✅ Maintain discipline (especially stop losses)
- ✅ Review and refine your process
- ✅ Keep learning and adapting

---

## 🤝 Contributing & Feedback

### Found a Bug?
- Check the Troubleshooting section first
- Verify your formulas match the documentation
- Document the issue with screenshots

### Have an Improvement?
- Share your modified formulas
- Explain your reasoning
- Test thoroughly before sharing

### Want to Share Results?
- Document your learnings
- Share anonymized performance data
- Help improve the system for everyone

---

## 📜 Version History

**v1.0** (October 2025)
- Initial release
- Three-tier classification system
- 25+ input metrics
- 5 component scores
- Tier-specific formulas and weights
- CSV import template
- Comprehensive documentation

---

## 🎓 Credits & Methodology

This system synthesizes best practices from:
- **Fundamental analysis** - Graham, Buffett, Lynch
- **Growth investing** - Fisher, O'Neil, ARK Invest
- **Quantitative scoring** - Piotroski F-Score, Magic Formula
- **Modern frameworks** - SaaS metrics, platform economics

**Built for:** Calculated aggressive growth investors
**Optimized for:** Tech and high-growth sectors
**Time horizon:** 3-5 year holding periods
**Risk tolerance:** Moderate to high

---

## 🚀 Ready to Get Started?

1. **Read:** `QUICK_START_IMPORT.md` (5 minutes)
2. **Import:** `stock_rating_template.csv` to Google Sheets
3. **Format:** Apply colors and conditional formatting
4. **Test:** Score 2-3 stocks you know
5. **Use:** Build your portfolio scoring system!

**Questions?** Check the comprehensive user guide for detailed explanations.

**Good luck, and happy investing!** 📈

---

**System:** Single-Sheet Stock Rating System v1.0
**Platform:** Google Sheets / Excel 2016+
**Created:** October 2025
**License:** For personal use
