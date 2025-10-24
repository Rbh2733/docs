# 3-TIER STOCK RATING SYSTEM - COMPLETE SCORING GUIDE

## TABLE OF CONTENTS
1. [Quick Start](#quick-start)
2. [Tier 1 (Core) - Detailed Scoring Methods](#tier-1-core)
3. [Tier 2 (Emerging) - Detailed Scoring Methods](#tier-2-emerging)
4. [Tier 3 (Moonshots) - Detailed Scoring Methods](#tier-3-moonshots)
5. [Data Sources & Tools](#data-sources-tools)
6. [Example Scorecards](#example-scorecards)
7. [Frequently Asked Questions](#faq)

---

## QUICK START

### Your First 30 Minutes

1. **Open the spreadsheet files in Excel or Google Sheets**
   - Import all CSV files as separate tabs
   - Review the default weights in Config & Weights tab
   - Default portfolio targets: 45% Core / 30% Emerging / 20% Moonshots / 5% Cash

2. **Start with Tier 1** - Your core holdings
   - Enter 3-5 of your largest positions
   - Focus on getting comfortable with one stock first

3. **Follow the example** for GOOGL to see how scoring works

4. **Check the Dashboard** to see how everything connects

### Example: Scoring GOOGL (Tier 1)

**Step 1: Gather Data**
- Current Price: $140
- Forward P/E: 22
- 5-year avg P/E: 25
- Revenue Growth: 12%
- Operating Margin: 32%
- FCF: $75B annually
- Market Cap: $1.8T

**Step 2: Calculate Component Scores**

**Valuation Score:**
- Forward P/E: 22 vs 25 historical = 12% discount → 85 points
- FCF Yield: ($75B / $1,800B) = 4.2% → 70 points
- PEG: 22 / 12 = 1.83 → 60 points
- **Average: 72 points**

**Quality Score:**
- ROIC: 28% → 100 points
- Operating Margin: 32% → 100 points
- Moat: Network effects + scale → +20 bonus → 100 points
- **Score: 95 points**

**Growth Score:**
- Revenue Growth: 12% → 55 points
- TAM: $500B+ remaining → +15 bonus
- **Score: 70 points**

**Momentum Score:**
- 12-month return: 35% → 80 points
- Above 200-day MA → 100 points
- **Average: 90 points**

**Financial Health:**
- Net Cash: $100B+ → 100 points
- **Score: 100 points**

**Step 3: Spreadsheet Calculates Composite**
- System applies weights: (72×0.20) + (95×0.30) + (70×0.30) + (90×0.10) + (100×0.10)
- **COMPOSITE SCORE: 82.4 → Buy Rating ⭐⭐⭐⭐**

---

## TIER 1 (CORE)

### Component Weights
- Valuation: 20%
- Quality: 30%
- Growth: 30%
- Momentum: 10%
- Financial Health: 10%

### VALUATION SCORE (0-100)

#### P/E Ratio Analysis

**Data needed:**
- Forward P/E (Yahoo Finance, Seeking Alpha)
- 5-year average P/E (Macrotrends)

**Scoring:**
```
If current P/E < historical average:
  Score = 100 (capped)

If current P/E > historical average:
  Score = 100 - [(Current / Historical) - 1] × 100

Example: Current 30, Historical 25
  Score = 100 - [(30/25) - 1] × 100 = 80
```

**Red Flags:**
- P/E > 40 for established companies
- P/E declining while price rises

#### Free Cash Flow Yield

**Formula:** FCF / Market Cap

**Scoring:**
- FCF Yield > 6%: 100 points
- FCF Yield 4-6%: 80 points
- FCF Yield 2-4%: 60 points
- FCF Yield 0-2%: 40 points
- Negative FCF: 20 points

**Sources:**
- Seeking Alpha → Financials → Cash Flow
- Company 10-K/10-Q filings

#### PEG Ratio

**Formula:** Forward P/E / Expected Growth Rate

**Scoring:**
- PEG < 1.0: 100 points
- PEG 1.0-1.5: 85 points
- PEG 1.5-2.0: 70 points
- PEG 2.0-2.5: 50 points
- PEG > 2.5: 30 points

---

### QUALITY SCORE (0-100)

#### Return on Invested Capital (ROIC)

**Formula:** NOPAT / (Total Debt + Equity - Cash)

**Scoring:**
- ROIC > 25%: 100 points
- ROIC 20-25%: 90 points
- ROIC 15-20%: 75 points
- ROIC 10-15%: 50 points
- ROIC < 10%: 25 points

**Shortcut:** GuruFocus.com → Financials → Profitability

#### Operating Margin

**Formula:** Operating Income / Revenue

**Scoring:**
- > 30%: 100 points
- 20-30%: 85 points
- 15-20%: 70 points
- 10-15%: 50 points
- < 10%: 30 points

**Adjust by industry:**
- Tech/Software: Expect 25-40%
- Retail: Expect 5-10%
- Manufacturing: Expect 10-20%

#### Competitive Moat

**Bonuses:**
- Network Effects: +20 (Google, Facebook, Visa)
- Economies of Scale: +15 (Amazon, Walmart)
- Switching Costs: +15 (Adobe, Salesforce)
- Intangible Assets: +10 (Apple brand, patents)

**Total Moat Score:** Add applicable bonuses, cap at +25

---

### GROWTH SCORE (0-100)

#### Revenue Growth (3-year CAGR)

**Formula:** (Ending Revenue / Beginning Revenue)^(1/3) - 1

**Scoring:**
- > 25%: 100 points
- 20-25%: 90 points
- 15-20%: 75 points
- 10-15%: 55 points
- 5-10%: 35 points
- < 5%: 15 points

#### Earnings Growth (3-year EPS CAGR)

**Scoring:**
- > 30%: 100 points
- 20-30%: 85 points
- 15-20%: 70 points
- 10-15%: 50 points
- < 10%: 30 points

**Important:** If earnings growth >> revenue growth → Operating leverage (good)

#### Total Addressable Market (TAM)

**Scoring:**
- TAM >$500B + <20% share: +15 bonus
- TAM $200-500B + <30% share: +10 bonus
- TAM <$200B or >40% share: 0 bonus

**Sources:**
- Company investor presentations
- Gartner/IDC reports
- Earnings call transcripts

---

### MOMENTUM SCORE (0-100)

#### 12-Month Price Return

**Calculation:** (Current Price - Price 12 months ago) / Price 12 months ago

**Scoring:**
- > 40%: 100 points
- 20-40%: 80 points
- 0-20%: 60 points
- -10 to 0%: 40 points
- < -10%: 60 points (potential reversal)

#### Relative Strength vs QQQ

**Scoring:**
- Outperform by >15%: 100 points
- Outperform by 0-15%: 75 points
- Underperform by 0-15%: 50 points
- Underperform by >15%: 30 points

#### Technical Setup

**Scoring:**
- Above both 50-day and 200-day MA: 100 points
- Above 200-day only: 70 points
- Between 50 and 200-day: 50 points
- Below both: 30 points

**Tools:** TradingView, Yahoo Finance, Stockcharts.com

---

### FINANCIAL HEALTH SCORE (0-100)

#### Net Cash Position

**Formula:** Cash + Marketable Securities - Total Debt

**Scoring (Mega-Caps):**
- Net cash >$50B: 100 points
- Net cash $25-50B: 90 points
- Net cash $0-25B: 80 points
- Net debt <$50B: 70 points
- Net debt >$50B: 50 points

#### Free Cash Flow Generation

**Scoring:**
- FCF >$15B annually: 100 points
- FCF $10-15B: 85 points
- FCF $5-10B: 70 points
- FCF <$5B: 50 points

**Note:** Adjust for company size if needed

---

## TIER 2 (EMERGING)

### Component Weights
- Valuation: 18%
- Quality: 25%
- Growth: 35% (HIGHEST - this is what you're paying for!)
- Momentum: 15%
- Scale & Moat: 7%

### Key Differences from Tier 1:
1. Lower profitability standards (accept 10-15% margins)
2. Higher growth expectations (want 25-40% growth)
3. New factor: Scale/Moat development
4. More tolerance for volatility

### VALUATION SCORE (0-100)

#### Flexible Approach

**If Profitable:** Use Forward P/E
- Forward P/E < 25: 100 points
- P/E 25-35: 85 points
- P/E 35-50: 70 points
- P/E 50-70: 50 points
- P/E > 70: 35 points

**If Pre-Profitable:** Use Price-to-Sales
- P/S < 8: 100 points
- P/S 8-15: 80 points
- P/S 15-25: 60 points
- P/S > 25: 40 points

#### PEG Ratio

Same as Tier 1, but more lenient:
- PEG of 2.0 is acceptable if growth is accelerating

---

### QUALITY SCORE (0-100)

#### Revenue Scale

**Scoring:**
- Revenue > $5B annually: 100 points
- Revenue $2-5B: 85 points
- Revenue $1-2B: 70 points
- Revenue $500M-$1B: 55 points
- Revenue < $500M: 40 points

#### Profitability Status

**Scoring:**
- GAAP profitable, >15% op margin: 100 points
- GAAP profitable, 10-15% margin: 85 points
- GAAP profitable, 5-10% margin: 70 points
- Non-GAAP profitable, GAAP breakeven: 60 points
- Path to profitability within 4 quarters: 50 points
- No clear path: 30 points

#### Gross Margin

**Scoring:**
- > 75%: 100 points (SaaS economics)
- 60-75%: 90 points
- 45-60%: 75 points (chip companies)
- 30-45%: 60 points
- < 30%: 40 points

**By Business Model:**
- Pure software: Expect 75-90%
- Cloud infrastructure: Expect 60-75%
- Semiconductors: Expect 45-65%

#### Customer Metrics (B2B/SaaS)

**Net Revenue Retention (NRR):**
- NRR > 120%: +20 bonus
- NRR 110-120%: +15 bonus
- NRR 100-110%: +10 bonus
- NRR < 100%: 0 bonus

**Sources:**
- Company earnings presentations
- Investor relations website

---

### GROWTH SCORE (0-100)

**HIGHEST WEIGHT (35%)** - This is the entire thesis!

#### Revenue Growth Rate (TTM)

**Scoring:**
- > 40%: 100 points
- 30-40%: 90 points
- 25-30%: 80 points
- 20-25%: 70 points
- 15-20%: 55 points
- 10-15%: 40 points
- < 10%: 20 points (not tier 2 material)

#### Growth Consistency

**Scoring:**
- Growing at 25%+ for 3 years: 100 points
- 2 years of 25%+: 85 points
- Accelerating from lower base: 80 points
- Volatile but averaging high: 60 points
- Decelerating: 40 points

#### TAM & Penetration

**Scoring:**
- TAM >$100B, <10% penetration: 100 points
- TAM $50-100B, <15% penetration: 85 points
- TAM $25-50B, <20% penetration: 70 points
- Significant runway: 100 points

#### Cyclicality Factor (for semiconductors, etc.)

**Scoring:**
- Non-cyclical: 100 points
- Early/mid cycle position: 85 points
- Late cycle but secular tailwinds: 70 points
- Peak cycle concerns: 40 points

---

### SCALE & MOAT SCORE (0-100)

**NEW FACTOR - Unique to Tier 2**

#### Competitive Position Evolution

**Scoring:**
- Pulling away from competition: 100 points
- Maintaining lead: 80 points
- Holding position: 60 points
- Losing ground: 30 points

#### Moat Development

**Bonuses:**
- Network effects developing: +25
- Switching costs emerging: +20
- Economies of scale: +15
- Strong ecosystem forming: +15

**Stack bonuses, cap at +30**

#### Operating Leverage

**Scoring:**
- Operating leverage inflecting: 100 points
- Early signs of leverage: 75 points
- Still investing heavily: 50 points

**What to look for:**
- Operating margin expanding faster than revenue growth
- Sales & Marketing % declining
- R&D efficiency improving

---

## TIER 3 (MOONSHOTS)

### Component Weights
- Valuation: 10% (LOWEST - you're paying for potential)
- Quality: 15%
- Growth: 45% (HIGHEST BY FAR!)
- Momentum: 20%
- Disruption Potential: 10%

### Philosophy: High Risk, High Reward
- **STRICT STOP LOSS: -40% from entry**
- Maximum position: 3%
- Focus on explosive growth and disruption

### VALUATION SCORE (0-100)

#### Price-to-Sales Focus

**Scoring:**
- P/S < 10x: 100 points
- P/S 10-20x: 85 points
- P/S 20-40x: 70 points
- P/S 40-60x: 50 points
- P/S > 60x: 30 points

**Note:** Even P/S of 50x can be acceptable if:
- Growth >75%
- Massive TAM
- Category-defining opportunity

#### Insider Ownership

**CRITICAL for moonshots**

**Scoring:**
- >15% insider ownership: +20 bonus
- 10-15%: +10 bonus
- 5-10%: 0
- <5%: -10 penalty (red flag!)

**Source:** Yahoo Finance → Statistics → Share Statistics

---

### QUALITY SCORE (0-100)

#### Gross Margin

**Scoring:**
- > 70%: 100 points (software economics)
- 50-70%: 85 points
- 30-50%: 60 points
- < 30%: 30 points

**Why this matters:** High gross margin = potential for profitability at scale

#### Revenue Quality

**Recurring/Subscription Revenue:**
- >70% recurring: +25 bonus
- 50-70% recurring: +15 bonus
- <50%: 0 bonus

**Customer Concentration:**
- <10% from top customer: +10 bonus
- 10-25%: 0
- >25%: -10 penalty (risk!)

#### Unit Economics

**LTV/CAC Ratio:**
- LTV/CAC > 3x: 100 points
- LTV/CAC 2-3x: 75 points
- LTV/CAC 1-2x: 40 points
- Not profitable yet but improving: 60 points

**Sources:** Company investor presentations, S-1 filings

#### Path to Profitability

**Scoring:**
- Already profitable: 100 points
- Profitable within 12 months: 80 points
- Profitable within 24 months: 60 points
- No clear path: 30 points

---

### GROWTH SCORE (0-100)

**HIGHEST WEIGHT (45%)** - This is the entire thesis!

#### Revenue Growth Rate

**Scoring:**
- > 100%: 100 points (hypergrowth!)
- 75-100%: 95 points
- 50-75%: 85 points
- 30-50%: 70 points
- 20-30%: 50 points
- < 20%: 25 points (not moonshot material)

#### Growth Consistency

**Scoring:**
- Accelerating for 3+ quarters: +25 bonus
- Accelerating for 2 quarters: +15 bonus
- Stable high growth: 0
- Decelerating: -20 penalty

#### TAM Size

**Scoring:**
- >$100B TAM: 100 points
- $50-100B: 85 points
- $25-50B: 70 points
- $10-25B: 50 points
- < $10B: 30 points (too small to matter)

#### Market Penetration

**Scoring:**
- <5% of TAM captured: 100 points (massive runway!)
- 5-10%: 85 points
- 10-20%: 70 points
- >20%: 50 points

**The lower the better** - means more room to grow

---

### MOMENTUM SCORE (0-100)

**HIGHER THAN OTHER TIERS (20%)** - Want to ride winners

#### 6-Month Price Performance

**Scoring:**
- > 100%: 100 points (rocket ship!)
- 50-100%: 90 points
- 25-50%: 75 points
- 0-25%: 50 points
- Negative but strong fundamentals: 40 points

#### Relative Strength vs Small-Cap Growth

Use IWO (Russell 2000 Growth) as benchmark

**Scoring:**
- Outperform by >30%: 100 points
- Outperform by 15-30%: 80 points
- Outperform by 0-15%: 60 points
- Underperform: 30 points

#### Social Sentiment / Buzz

**Bonuses:**
- StockTwits rising mentions + positive: +20
- Reddit positive discussion: +10
- >3 analyst upgrades in quarter: +15
- Positive CNBC/Bloomberg coverage: +10

#### Volume Surge

**Scoring:**
- Average volume up 50%+: 100 points
- Volume up 20-50%: 75 points
- Stable volume: 50 points
- Declining volume: 30 points

**What this means:** Volume surge = institutions accumulating

---

### DISRUPTION POTENTIAL SCORE (0-100)

**UNIQUE TO TIER 3** - Assessing paradigm shift potential

#### Market Disruption

**Scoring:**
- Attacking $100B+ entrenched market: 100 points
- Creating new market category: 95 points
- Significant share gains from legacy: 85 points
- Incremental improvement: 50 points

**Examples:**
- RKLB: Creating cheap space access → 95 points
- IONQ: Creating quantum computing → 95 points

#### Technology Moat

**Bonuses:**
- Proprietary AI/ML advantage: +20
- Patent portfolio: +15
- Unique data assets: +15
- First-mover with scale: +10

#### Competitive Dynamics

**Scoring:**
- Winner-take-most market: 100 points
- Few viable competitors (oligopoly): 80 points
- Crowded but differentiated: 60 points
- Commodity risk: 30 points

#### Catalyst Pipeline

**Bonuses:**
- Major product launches next 6 months: +15
- Partnership announcements pending: +10
- Market expansion planned: +10
- Regulatory approval expected: +15

---

## DATA SOURCES & TOOLS

### Free Resources

**Financial Data:**
- **Yahoo Finance** - Prices, basics, earnings history
- **Seeking Alpha** - Detailed financials, estimates
- **Finviz** - Screener, sector comparison
- **Macrotrends** - Historical data, charts
- **GuruFocus** - ROIC, quality metrics

**SEC Filings:**
- **SEC.gov/EDGAR** - 10-K, 10-Q, 8-K, DEF 14A
- Company investor relations websites

**Market Data:**
- **TradingView** - Charts, technical analysis
- **Stockcharts.com** - Technical indicators

**Institutional Data:**
- **WhaleWisdom** - 13F filings
- **Fintel.io** - Insider trading, ownership

**News & Analysis:**
- Company earnings call transcripts
- Seeking Alpha articles
- Financial Twitter

**Industry Research:**
- Gartner Magic Quadrant (tech sectors)
- IDC, Forrester (market sizing)

### Paid Tools (Optional)

**Koyfin** ($30-50/month)
- Comprehensive financials
- Easy comp tables
- Custom dashboards

**YCharts** ($200+/month)
- Professional-grade data
- Sector analysis
- Export to Excel

**FactSet / Bloomberg Terminal** ($2,000+/month)
- Institutional grade
- Only if managing large portfolio

---

## EXAMPLE SCORECARDS

### Example 1: GOOGL (Tier 1 - Core)

**Date Scored:** October 2025
**Current Price:** $140
**Market Cap:** $1.8T

**INPUT DATA:**
- Forward P/E: 22
- 5-year avg P/E: 25
- FCF: $75B
- Revenue Growth: 12%
- EPS Growth: 15%
- Operating Margin: 32%
- ROIC: 28%
- Net Cash: $100B
- 12-month return: 35%

**SCORING:**

| Component | Score | Calculation |
|-----------|-------|-------------|
| **Valuation (20%)** | 72 | P/E:85, FCF Yield:70, PEG:60 |
| **Quality (30%)** | 95 | ROIC:100, Margin:100, Moat:100 |
| **Growth (30%)** | 70 | Rev:55, EPS:70, TAM bonus |
| **Momentum (10%)** | 90 | 12M:80, Technical:100 |
| **Financial Health (10%)** | 100 | Net Cash:100, FCF:100 |

**COMPOSITE:** (72×0.20) + (95×0.30) + (70×0.30) + (90×0.10) + (100×0.10) = **84.1**

**RATING: Buy ⭐⭐⭐⭐**
**TARGET ALLOCATION: 12%**

---

### Example 2: PLTR (Tier 2 - Emerging)

**Date Scored:** October 2025
**Current Price:** $28
**Market Cap:** $65B

**INPUT DATA:**
- P/S: 22x
- Revenue: $2.5B (30% growth)
- Operating Margin: 15% (expanding)
- NRR: 115%
- Beta: 1.8
- 6-month return: 55%

**SCORING:**

| Component | Score | Calculation |
|-----------|-------|-------------|
| **Valuation (18%)** | 61 | P/S:60, PEG:75 |
| **Quality (25%)** | 89 | Scale:85, Margin:100, NRR bonus |
| **Growth (35%)** | 92 | Rev:90, TAM:100, Drivers bonus |
| **Momentum (15%)** | 93 | 6M:85, Rel Strength:100 |
| **Scale/Moat (7%)** | 98 | Position:100, Moat bonus |

**COMPOSITE:** = **86.4**

**RATING: Strong Buy ⭐⭐⭐⭐⭐**
**TARGET ALLOCATION: 6%**

---

### Example 3: RKLB (Tier 3 - Moonshot)

**Date Scored:** October 2025
**Current Price:** $9.50
**Market Cap:** $4.5B
**Entry Price:** $8.20
**STOP LOSS:** $4.92 (-40%)

**INPUT DATA:**
- P/S: 28x
- Revenue: $150M (85% growth!)
- Gross Margin: 55%
- Not profitable (path in 2026)
- Launch cadence increasing
- Beta: 2.3

**SCORING:**

| Component | Score | Calculation |
|-----------|-------|-------------|
| **Valuation (10%)** | 78 | P/S:70, Insider:90 |
| **Quality (15%)** | 75 | Margin:85, Path:80 |
| **Growth (45%)** | 94 | Rev:95, TAM:100, Penetration:100 |
| **Momentum (20%)** | 96 | 6M:100, Volume:100 |
| **Disruption (10%)** | 93 | Market:95, Tech:90 |

**COMPOSITE:** = **89.9**

**RATING: Strong Buy ⭐⭐⭐⭐⭐**
**TARGET ALLOCATION: 2-3%**
**RISK: HIGH - Monitor stop loss!**

---

## FAQ

### General Questions

**Q: How often should I update scores?**
A:
- Full scoring: Quarterly after earnings
- Momentum scores: Weekly
- Price/position updates: Daily or as needed
- Quick review: Monthly

**Q: What if I disagree with a component score?**
A: The system is a framework, not a prison. Adjust scores with documentation in the Notes field. But be honest about bias.

**Q: Should I sell immediately when a stock drops below the rating threshold?**
A: No. Use a "two quarter rule" for Core and Emerging holdings. If a stock scores below threshold for 2 consecutive quarters, then exit.

**Q: Can a stock be in multiple tiers?**
A: No. Each holding should be in one tier only. Use market cap and business maturity as the primary guide.

---

### Scoring Questions

**Q: What if I can't find data for a specific metric?**
A:
1. Try alternative sources (company presentations, earnings calls)
2. Use proxy metrics
3. Score conservatively (50 points) if truly unknown
4. Document in Notes that data is unavailable

**Q: Should all my stocks score 80+?**
A: No! A diversified portfolio will have a range:
- Core: Target average 80-85
- Emerging: Target average 75-80
- Moonshots: Target average 70-75

---

### Position Sizing Questions

**Q: The calculated position size seems too small. Can I override it?**
A: Yes, but carefully:
1. Ensure score is 75+
2. Have strong conviction
3. Don't exceed tier maximum
4. Accept higher volatility risk

**Q: How do I handle position drift from appreciation?**
A:
- Monthly: Trim if >10% over target
- Quarterly: Rebalance all positions >5% off target
- Let winners run within tier maximums

---

### Risk Management Questions

**Q: Do I really need stop losses on Tier 3?**
A: **YES.** This is non-negotiable. Moonshots can go to zero. The -40% hard stop protects capital. Stick to it.

**Q: What about stop losses on Tier 1?**
A: Not typically. Instead:
- Monitor scores quarterly
- Exit if score drops below 65
- Or if investment thesis breaks

---

### Portfolio Construction Questions

**Q: Should I fill all tier allocations immediately?**
A: No. Build gradually:
- Month 1: Establish 3-4 Core positions
- Month 2-3: Add remaining Core, start Emerging
- Month 4-6: Add Moonshots selectively

Only deploy capital into 75+ scores.

**Q: What if I can't find enough high-scoring stocks?**
A: That's a feature, not a bug. Keep standards high:
- Hold more cash (5-15%)
- Wait for better entries
- Don't force positions

**Q: How concentrated should I be?**
A: Guideline:
- Top 5 positions: 40-50% of portfolio
- Top 10 positions: 70-80% of portfolio
- Remaining 20-30%: Moonshots for diversification

---

## FINAL TIPS FOR SUCCESS

### 1. Start Simple
- Begin with just 5-10 positions
- Get comfortable with one tier at a time
- Don't overthink initial scores

### 2. Be Consistent
- Use same data sources
- Score at regular intervals
- Document your reasoning

### 3. Be Honest
- Don't inflate scores for stocks you like
- Accept when thesis breaks
- Emotion is the enemy

### 4. Review & Refine
- Track what worked/didn't quarterly
- Adjust weights based on results
- But don't change constantly

### 5. Focus on Process
- The score is the output
- Your research is the input
- Trust the system you built

### 6. Key Habits
- **Weekly:** Review prices, momentum, alerts
- **Monthly:** Update scores, check targets
- **Quarterly:** Full review, rebalance, tier reclassification
- **Annually:** Backtest, optimize weights

---

**The journey of a thousand trades begins with a single score.**

Good luck, and may your returns be outsized and your drawdowns minimal!

---

**Version:** 1.0
**Created:** October 2025
