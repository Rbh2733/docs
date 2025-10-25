# BUILD YOUR 3-TIER PORTFOLIO TRACKER - EXCEL
## Direct Implementation Guide (Excel Version)

---

## YOUR SYSTEM AT A GLANCE

**Philosophy:** Calculated aggressive growth via core-satellite structure
**Time to build:** 2-3 hours for complete system OR 90 min for MVP
**Maintenance:** 15 min/week, 1 hour/month, 3 hours/quarter

**The Promise:**
- Add stocks by typing. Formulas auto-apply (Excel Tables).
- Delete rows anytime. Nothing breaks.
- Change weights once. Everything updates.
- Execute stop losses without emotion.
- Build legacy wealth systematically.

**Excel Version Notes:**
- Uses **Excel Tables** instead of ARRAYFORMULA for auto-expanding formulas
- Dynamic arrays (Excel 365) or traditional formulas for older versions
- Named ranges work the same way
- Conditional formatting has different menus but same power

---

## PHASE 1: FOUNDATION (30 MIN)

### Step 1: Create Workbook (5 min)

1. Open **Excel** (Desktop or Excel 365)
2. Click **Blank Workbook**
3. Save as: **"3-Tier Portfolio Tracker.xlsx"**
4. Create these sheets (click + or right-click tabs):
   - Config & Weights
   - Tier 1 - Core
   - Tier 2 - Emerging
   - Tier 3 - Moonshots
   - Dashboard
   - Instructions

---

### Step 2: Build Config & Weights (10 min)

Copy-paste this EXACTLY into Config & Weights sheet:

**Row 1-3: Headers**
```
A1: 3-TIER STOCK RATING SYSTEM
A2: Configuration & Weights
A3: Last Updated: [Today's Date]
```

**Row 5-11: Tier 1 Weights**
```
A5: TIER 1 - CORE HOLDINGS WEIGHTS
A6: Valuation        C6: 0.20
A7: Quality          C7: 0.30
A8: Growth           C8: 0.30
A9: Momentum         C9: 0.10
A10: Financial Health C10: 0.10
A11: TOTAL           C11: =SUM(C6:C10)
```

**Row 13-19: Tier 2 Weights**
```
A13: TIER 2 - EMERGING LEADERS WEIGHTS
A14: Valuation       C14: 0.18
A15: Quality         C15: 0.25
A16: Growth          C16: 0.35
A17: Momentum        C17: 0.15
A18: Scale/Moat      C18: 0.07
A19: TOTAL           C19: =SUM(C14:C18)
```

**Row 21-27: Tier 3 Weights**
```
A21: TIER 3 - MOONSHOTS WEIGHTS
A22: Valuation       C22: 0.10
A23: Quality         C23: 0.15
A24: Growth          C24: 0.45
A25: Momentum        C25: 0.20
A26: Disruption      C26: 0.10
A27: TOTAL           C27: =SUM(C22:C26)
```

**Row 29-33: Targets**
```
A29: PORTFOLIO ALLOCATION TARGETS
A30: Tier 1 (Core)      B30: 45%
A31: Tier 2 (Emerging)  B31: 30%
A32: Tier 3 (Moonshots) B32: 20%
A33: Cash               B33: 5%
```

**Format:**
- Bold all header rows (5, 13, 21, 29)
- A1: Size 18, bold
- Gray background on headers

---

### Step 3: Create Named Ranges (15 min)

**CRITICAL STEP - Makes everything bulletproof**

**In Excel:**
- Select cell → Formulas tab → Define Name
- OR use Name Box (left of formula bar)

**Tier 1 Weights:**
```
Tier1_Val_Weight → 'Config & Weights'!$C$6
Tier1_Qual_Weight → 'Config & Weights'!$C$7
Tier1_Growth_Weight → 'Config & Weights'!$C$8
Tier1_Mom_Weight → 'Config & Weights'!$C$9
Tier1_FinHealth_Weight → 'Config & Weights'!$C$10
```

**Tier 2 Weights:**
```
Tier2_Val_Weight → 'Config & Weights'!$C$14
Tier2_Qual_Weight → 'Config & Weights'!$C$15
Tier2_Growth_Weight → 'Config & Weights'!$C$16
Tier2_Mom_Weight → 'Config & Weights'!$C$17
Tier2_Moat_Weight → 'Config & Weights'!$C$18
```

**Tier 3 Weights:**
```
Tier3_Val_Weight → 'Config & Weights'!$C$22
Tier3_Qual_Weight → 'Config & Weights'!$C$23
Tier3_Growth_Weight → 'Config & Weights'!$C$24
Tier3_Mom_Weight → 'Config & Weights'!$C$25
Tier3_Disrupt_Weight → 'Config & Weights'!$C$26
```

**TEST:** In any cell, type `=Tier1_Val_Weight` → Should show **0.2** ✓

---

## PHASE 2: TIER 1 - CORE (30 MIN)

### Column Headers (Row 4)

```
A4: Ticker
B4: Company
C4: Price
D4: Market Value
E4: Valuation
F4: Quality
G4: Growth
H4: Momentum
I4: Fin Health
J4: Composite
K4: Rating
L4: Action
M4: % Portfolio
N4: Notes
```

**Format:**
- Bold, center-align
- **CRITICAL:** Select A4:N4, then Insert → Table (or Ctrl+T)
  - Check "My table has headers"
  - This enables auto-expanding formulas!
- Freeze row 4: View → Freeze Panes → Freeze Top Row

---

### EXCEL APPROACH: Using Tables for Auto-Expanding Formulas

**Two methods depending on your Excel version:**

#### METHOD 1: Excel 365/2021 (Dynamic Arrays - RECOMMENDED)

**J5 - Composite Score:**
```
=IF(E5="",,E5*Tier1_Val_Weight+F5*Tier1_Qual_Weight+G5*Tier1_Growth_Weight+H5*Tier1_Mom_Weight+I5*Tier1_FinHealth_Weight)
```
Enter in J5, it will auto-copy down in the Table.

**K5 - Rating:**
```
=IF(J5="",,IF(J5>=85,"★★★★★ Strong Buy",IF(J5>=75,"★★★★ Buy",IF(J5>=65,"★★★ Hold",IF(J5>=55,"★★ Reduce","★ Exit")))))
```

**L5 - Action Signal:**
```
=IF(J5="",,IF(J5>=80,"🟢 ADD",IF(J5>=75,"🟡 HOLD",IF(J5>=65,"🟠 WATCH","🔴 EXIT"))))
```

**In Excel Tables, these formulas automatically copy down when you add new rows!**

---

#### METHOD 2: Older Excel (2016/2019)

**Option A - Use Table structured references:**
Same formulas as above, but you'll need to:
1. Enter formula in J5
2. Copy formula down to J100 (or drag fill handle)
3. Repeat for K5, L5

**Option B - Traditional fill-down:**
1. Enter formula in J5
2. Select J5:J100
3. Ctrl+D to fill down
4. Formulas will show blank if source cells are empty (due to IF statement)

---

### Create Column Named Ranges

**Formulas → Name Manager → New:**

```
Tier1_Ticker → 'Tier 1 - Core'!$A:$A
Tier1_MarketValue → 'Tier 1 - Core'!$D:$D
Tier1_Composite → 'Tier 1 - Core'!$J:$J
Tier1_Rating → 'Tier 1 - Core'!$K:$K
```

**Note:** If using Tables, Excel auto-creates structured references:
- Table name will be something like `Table1`
- You can rename: Table Design → Table Name → "Tier1_Table"
- Then reference columns as: `Tier1_Table[Composite]`

---

### Test Your Setup

Add this in Row 5:
```
A5: GOOGL
B5: Alphabet
C5: 140
D5: 25000
E5: 75
F5: 95
G5: 70
H5: 85
I5: 100
```

**Expected Results:**
- J5: ~85.5 (will show green with conditional formatting)
- K5: ★★★★★ Strong Buy
- L5: 🟢 ADD

**Now add same stock in row 10. Then delete row 5.**
→ Everything still works? ✓ You're good.

---

## PHASE 3: TIER 2 - EMERGING (25 MIN)

### Column Headers (Row 4)

```
A4: Ticker
B4: Company
C4: Price
D4: Market Value
E4: Valuation
F4: Quality
G4: Growth
H4: Momentum
I4: Scale/Moat
J4: Beta
K4: Vol Factor
L4: Composite
M4: Calc Position
N4: Rating
O4: Action
P4: Notes
```

**Convert to Table:** Select A4:P4 → Insert → Table

---

### Formulas (Excel Version)

**K5 - Volatility Factor:**
```
=IF(J5="",,IF(J5<1.5,1,IF(J5<2,1.2,IF(J5<2.5,1.4,1.8))))
```

**L5 - Composite:**
```
=IF(E5="",,E5*Tier2_Val_Weight+F5*Tier2_Qual_Weight+G5*Tier2_Growth_Weight+H5*Tier2_Mom_Weight+I5*Tier2_Moat_Weight)
```

**M5 - Calculated Position:**
```
=IF(L5="",,ROUND((L5/100)*6/K5,2))
```

**N5 - Rating:**
```
=IF(L5="",,IF(L5>=85,"★★★★★ Strong Buy",IF(L5>=75,"★★★★ Buy",IF(L5>=65,"★★★ Accumulate",IF(L5>=55,"★★ Hold","★ Exit")))))
```

**O5 - Action:**
```
=IF(L5="",,IF(L5>=80,"🟢 ADD",IF(L5>=75,"🟡 HOLD",IF(L5>=65,"🟠 ACCUMULATE","🔴 EXIT"))))
```

**If using Excel Table, formulas auto-copy. Otherwise, copy down to row 100.**

---

### Named Ranges

```
Tier2_MarketValue → 'Tier 2 - Emerging'!$D:$D
Tier2_Beta → 'Tier 2 - Emerging'!$J:$J
Tier2_Composite → 'Tier 2 - Emerging'!$L:$L
Tier2_Rating → 'Tier 2 - Emerging'!$N:$N
```

---

### Test

```
Row 5:
A5: PLTR    C5: 28    E5: 65
B5: Palantir D5: 8000  F5: 85
                       G5: 90
J5: 1.8                H5: 95
                       I5: 90
```

Expected: L5: ~86.4, M5: ~4.0%, N5: Strong Buy

---

## PHASE 4: TIER 3 - MOONSHOTS (30 MIN)

### Column Headers (Row 4)

```
A4: Ticker
B4: Company
C4: Price
D4: Market Value
E4: Valuation
F4: Quality
G4: Growth
H4: Momentum
I4: Disruption
J4: Beta
K4: Vol Factor
L4: Entry Price
M4: Stop Loss
N4: Composite
O4: Calc Position
P4: Rating
Q4: Action
R4: 🚨 STOP ALERT
S4: Notes
```

**Convert to Table:** Select A4:S4 → Insert → Table

---

### Formulas (Excel Version)

**K5 - Volatility Factor:**
```
=IF(J5="",,IF(J5<1.5,1,IF(J5<2.5,1.4,IF(J5<3,1.6,1.8))))
```

**M5 - Stop Loss (40% below entry):**
```
=IF(L5="",,ROUND(L5*0.6,2))
```

**N5 - Composite:**
```
=IF(E5="",,E5*Tier3_Val_Weight+F5*Tier3_Qual_Weight+G5*Tier3_Growth_Weight+H5*Tier3_Mom_Weight+I5*Tier3_Disrupt_Weight)
```

**O5 - Calculated Position:**
```
=IF(N5="",,ROUND((N5/100)*3/K5,2))
```

**P5 - Rating:**
```
=IF(N5="",,IF(N5>=80,"★★★★★ Strong Buy",IF(N5>=70,"★★★★ Buy",IF(N5>=65,"★★★ Spec Buy",IF(N5>=60,"★★ Watch",IF(N5>=50,"★ Watch","❌ Pass"))))))
```

**Q5 - Action:**
```
=IF(N5="",,IF(N5>=80,"🟢 STRONG ADD",IF(N5>=70,"🟢 ADD",IF(N5>=65,"🟡 SPEC BUY",IF(N5>=60,"🟠 WATCH","🔴 PASS")))))
```

**R5 - CRITICAL STOP LOSS ALERT:**
```
=IF(C5="",,IF(C5<=M5,"🚨 HIT STOP LOSS - SELL NOW",IF(C5<=M5*1.1,"⚠️ Near Stop Loss",IF(C5<=M5*1.2,"⚡ Watch Closely",""))))
```

---

### Named Ranges

```
Tier3_Ticker → 'Tier 3 - Moonshots'!$A:$A
Tier3_Price → 'Tier 3 - Moonshots'!$C:$C
Tier3_MarketValue → 'Tier 3 - Moonshots'!$D:$D
Tier3_StopLoss → 'Tier 3 - Moonshots'!$M:$M
Tier3_Composite → 'Tier 3 - Moonshots'!$N:$N
Tier3_Rating → 'Tier 3 - Moonshots'!$P:$P
Tier3_Alert → 'Tier 3 - Moonshots'!$R:$R
```

---

### Test (CRITICAL - Stop Loss Mechanics)

```
Row 5:
A5: RKLB     C5: 9.50   E5: 70   J5: 2.3
B5: Rocket Lab D5: 1200 F5: 75   L5: 8.20
                        G5: 95
                        H5: 100
                        I5: 90
```

Expected:
- M5: $4.92 (stop loss)
- N5: ~89.9
- R5: Blank (price above stop)

**Now change C5 to 4.80:**
- R5: 🚨 HIT STOP LOSS - SELL NOW
- Cell should be BRIGHT RED (after conditional formatting)

✓ This is your discipline enforcer.

---

## PHASE 5: DASHBOARD (30 MIN)

### Layout

```
A1: 📊 PORTFOLIO DASHBOARD
A2: =TODAY()

A4: PORTFOLIO SUMMARY
A5: Total Portfolio Value:    B5: [formula below]
A6: Tier 1 Value:              B6: [formula below]
A7: Tier 2 Value:              B7: [formula below]
A8: Tier 3 Value:              B8: [formula below]
A9: Cash:                      B9: [ENTER MANUALLY]

A11: ALLOCATION %
A12: Tier 1 Actual:    B12: [formula]    C12: Target:  D12: 45%
A13: Tier 2 Actual:    B13: [formula]    C13: Target:  D13: 30%
A14: Tier 3 Actual:    B14: [formula]    C14: Target:  D14: 20%
A15: Cash Actual:      B15: [formula]    C15: Target:  D15: 5%

A17: WEIGHTED SCORES
A18: Tier 1 Avg:       B18: [formula]
A19: Tier 2 Avg:       B19: [formula]
A20: Tier 3 Avg:       B20: [formula]
A21: Overall Score:    B21: [formula]

A23: ACTION ITEMS
A24: Positions to EXIT:        B24: [formula]
A25: Positions to ADD:         B25: [formula]
A26: Tier 3 Near Stop:         B26: [formula]
```

---

### Formulas (Excel Version)

**Excel Difference:** FILTER function availability depends on version.

#### For Excel 365 (has FILTER function):

**B5 - Total Portfolio:**
```
=SUM(FILTER(Tier1_MarketValue,Tier1_MarketValue<>""))+SUM(FILTER(Tier2_MarketValue,Tier2_MarketValue<>""))+SUM(FILTER(Tier3_MarketValue,Tier3_MarketValue<>""))+Cash_Value
```

**B6-B8 - Tier Values:**
```
B6: =SUM(FILTER(Tier1_MarketValue,Tier1_MarketValue<>""))
B7: =SUM(FILTER(Tier2_MarketValue,Tier2_MarketValue<>""))
B8: =SUM(FILTER(Tier3_MarketValue,Tier3_MarketValue<>""))
```

---

#### For Excel 2016/2019 (no FILTER - use SUMIF):

**B5 - Total Portfolio:**
```
=SUMIF(Tier1_MarketValue,"<>",Tier1_MarketValue)+SUMIF(Tier2_MarketValue,"<>",Tier2_MarketValue)+SUMIF(Tier3_MarketValue,"<>",Tier3_MarketValue)+Cash_Value
```

**B6-B8 - Tier Values:**
```
B6: =SUMIF(Tier1_MarketValue,"<>",Tier1_MarketValue)
B7: =SUMIF(Tier2_MarketValue,"<>",Tier2_MarketValue)
B8: =SUMIF(Tier3_MarketValue,"<>",Tier3_MarketValue)
```

---

**Create these named ranges NOW:**
```
Total_Portfolio_Value → Dashboard!$B$5
Cash_Value → Dashboard!$B$9
```

**B12-B15 - Allocation % (Same for all versions):**
```
B12: =IF(Total_Portfolio_Value=0,0,B6/Total_Portfolio_Value)
B13: =IF(Total_Portfolio_Value=0,0,B7/Total_Portfolio_Value)
B14: =IF(Total_Portfolio_Value=0,0,B8/Total_Portfolio_Value)
B15: =IF(Total_Portfolio_Value=0,0,Cash_Value/Total_Portfolio_Value)
```
Format as percentage (Ctrl+Shift+%)

---

### Weighted Scores

#### For Excel 365 (with FILTER):

**B18-B20:**
```
B18: =IFERROR(SUMPRODUCT(FILTER(Tier1_MarketValue,Tier1_MarketValue<>""),FILTER(Tier1_Composite,Tier1_Composite<>""))/SUM(FILTER(Tier1_MarketValue,Tier1_MarketValue<>"")),0)

B19: =IFERROR(SUMPRODUCT(FILTER(Tier2_MarketValue,Tier2_MarketValue<>""),FILTER(Tier2_Composite,Tier2_Composite<>""))/SUM(FILTER(Tier2_MarketValue,Tier2_MarketValue<>"")),0)

B20: =IFERROR(SUMPRODUCT(FILTER(Tier3_MarketValue,Tier3_MarketValue<>""),FILTER(Tier3_Composite,Tier3_Composite<>""))/SUM(FILTER(Tier3_MarketValue,Tier3_MarketValue<>"")),0)
```

#### For Excel 2016/2019 (without FILTER):

**B18-B20:**
```
B18: =IFERROR(SUMPRODUCT((Tier1_MarketValue<>"")*Tier1_MarketValue,(Tier1_Composite<>"")*Tier1_Composite)/SUMIF(Tier1_MarketValue,"<>"),0)

B19: =IFERROR(SUMPRODUCT((Tier2_MarketValue<>"")*Tier2_MarketValue,(Tier2_Composite<>"")*Tier2_Composite)/SUMIF(Tier2_MarketValue,"<>"),0)

B20: =IFERROR(SUMPRODUCT((Tier3_MarketValue<>"")*Tier3_MarketValue,(Tier3_Composite<>"")*Tier3_Composite)/SUMIF(Tier3_MarketValue,"<>"),0)
```

---

**B21 - Overall Score (Same for all versions):**
```
=IFERROR((B18*B12+B19*B13+B20*B14)/(B12+B13+B14),0)
```

---

### Action Items

#### For Excel 365 (with FILTER):

**B24-B26:**
```
B24: =SUMPRODUCT((Tier1_Composite<75)*(Tier1_Composite>0))+SUMPRODUCT((Tier2_Composite<65)*(Tier2_Composite>0))+SUMPRODUCT((Tier3_Composite<50)*(Tier3_Composite>0))

B25: =SUMPRODUCT(COUNTIF(Tier1_Rating,"*Strong Buy*"))+SUMPRODUCT(COUNTIF(Tier2_Rating,"*Strong Buy*"))+SUMPRODUCT(COUNTIF(Tier3_Rating,"*Strong Buy*"))

B26: =COUNTIF(Tier3_Alert,"*Stop Loss*")
```

#### For Excel 2016/2019:

**B24:**
```
=COUNTIFS(Tier1_Composite,"<75",Tier1_Composite,">0")+COUNTIFS(Tier2_Composite,"<65",Tier2_Composite,">0")+COUNTIFS(Tier3_Composite,"<50",Tier3_Composite,">0")
```

**B25:**
```
=COUNTIF(Tier1_Rating,"*Strong Buy*")+COUNTIF(Tier2_Rating,"*Strong Buy*")+COUNTIF(Tier3_Rating,"*Strong Buy*")
```

**B26:**
```
=COUNTIF(Tier3_Alert,"*Stop Loss*")
```

---

### NOW Go Back to Tier 1

**Add M5 formula (Portfolio %):**
```
=IF(D5="",,D5/Total_Portfolio_Value)
```

If using Table, enter in M5 and it auto-copies down.

---

## PHASE 6: CONDITIONAL FORMATTING (20 MIN)

**Excel Path:** Home → Conditional Formatting

### Tier 1: Composite Score Color Scale

1. Select **J5:J1000**
2. Home → Conditional Formatting → Color Scales → More Rules
3. Format Style: 3-Color Scale
   - Minimum: Number 50 → Red
   - Midpoint: Number 75 → Yellow
   - Maximum: Number 100 → Green

### Tier 1: Rating Text Colors

1. Select **K5:K1000**
2. Conditional Formatting → New Rule → "Format only cells that contain"

**Create separate rules:**

**Rule 1 - Strong Buy:**
- Cell Value → contains → "Strong Buy"
- Format: Dark green fill (RGB 0,128,0), white bold text

**Rule 2 - Buy:**
- Cell Value → contains → "Buy"
- Format: Light green fill (RGB 146,208,80)

**Rule 3 - Hold:**
- Cell Value → contains → "Hold"
- Format: Yellow fill (RGB 255,255,0)

**Rule 4 - Exit:**
- Cell Value → contains → "Exit"
- Format: Red fill (RGB 255,0,0), white text

### Tier 1: Row Alert for Low Scores

1. Select **A5:N1000**
2. Conditional Formatting → New Rule → "Use a formula to determine which cells to format"
3. Formula: `=$J5<65`
4. Format: Light red background (RGB 255,199,206)

**Repeat for Tier 2 & 3** (adjust column letters):
- Tier 2: `=$L5<65` for range A5:P1000
- Tier 3: `=$N5<50` for range A5:S1000

---

### Tier 3: CRITICAL STOP LOSS ALERTS

**Select R5:R1000, create these rules (order matters!):**

**Rule 1 - HIT STOP (highest priority):**
- Cell Value → contains → "HIT STOP"
- Format:
  - Fill: Bright red (RGB 255,0,0)
  - Font: White, Bold, Size 12

**Rule 2 - Near Stop:**
- Cell Value → contains → "Near Stop"
- Format: Orange fill (RGB 255,192,0), bold

**Rule 3 - Watch Closely:**
- Cell Value → contains → "Watch Closely"
- Format: Yellow fill (RGB 255,255,0)

**Row highlighting when stop alert exists:**
1. Select **A5:S1000**
2. New Rule → Use formula: `=$R5<>""`
3. Format: Light red background

---

## PHASE 7: PROTECT FORMULAS (10 MIN)

### Excel Protection Method

**Tier 1:**

1. Select **J5:J1000** (Composite)
2. Right-click → Format Cells → Protection → Check "Locked"
3. Repeat for:
   - K5:K1000 (Rating)
   - L5:L1000 (Action)
   - M5:M1000 (Portfolio %)

4. After locking all formula cells:
   - Review → Protect Sheet
   - Uncheck "Select locked cells" (optional)
   - Set password (optional)

**Tier 2:**

Lock these ranges:
- K5:K1000 (Vol Factor)
- L5:L1000 (Composite)
- M5:M1000 (Calc Position)
- N5:N1000 (Rating)
- O5:O1000 (Action)

Then: Review → Protect Sheet

**Tier 3:**

Lock these ranges:
- K5:K1000 (Vol Factor)
- M5:M1000 (Stop Loss)
- N5:N1000 (Composite)
- O5:O1000 (Calc Position)
- P5:P1000 (Rating)
- Q5:Q1000 (Action)
- R5:R1000 (Alert)

Then: Review → Protect Sheet

**Dashboard:**

1. Unlock ONLY B9 (Cash entry):
   - Select B9 → Format Cells → Protection → Uncheck "Locked"
2. Review → Protect Sheet

---

## FINAL TEST (15 MIN)

### Test 1: Add New Position

1. Go to Tier 1
2. Type NVDA in row 15 (if using Table, formulas appear automatically)
3. Enter scores
4. Watch formulas calculate ✓
5. Check Dashboard updates ✓

### Test 2: Delete Position

1. Delete row 8 (right-click row → Delete)
2. Formulas still work? ✓
3. Dashboard still accurate? ✓
4. No #REF! errors? ✓

### Test 3: Stop Loss

1. Tier 3: Add test stock
2. Entry: $10, Current: $5.50
3. R column shows red alert? ✓
4. **This saves you from yourself**

---

## EXCEL-SPECIFIC TIPS

### Auto-Refresh with Stock Data Types (Excel 365 Only)

**Optional Enhancement:**

1. Select ticker column (A5:A100)
2. Data → Stocks (may need Microsoft 365 subscription)
3. Excel converts to stock data type
4. Add column: Click icon next to ticker → Price
5. Auto-updates from internet!

**Note:** This replaces manual price entry for Tier 1-3.

---

### Power Query Integration (Advanced)

**For automatic data refresh:**

1. Data → Get Data → From Other Sources → Blank Query
2. Use Power Query to fetch Yahoo Finance or other APIs
3. Refresh all data with one click

---

## YOU'RE DONE. NOW USE IT.

### Week 1 - Get Comfortable

- Enter your actual positions
- Score them (use Complete_Scoring_Guide.md)
- Watch the system work
- Build trust in calculations

### Week 2 - Establish Rhythm

- Monday AM: Update prices, check Tier 3 stops
- Update momentum scores
- Follow action signals

### Month 1 - See Results

- Execute first stop loss (you will feel it)
- Rebalance based on targets
- Refine weights if needed
- Trust the process

---

## YOUR OPERATING RULES

### Tier 1 - Core (40-50%)
- Max position: 15%
- No stop losses
- Exit if score <75 for 2 quarters
- Mega-caps: GOOGL, NVDA, MSFT, AMZN, META

### Tier 2 - Emerging (25-35%)
- Max position: 8%
- Stop loss: -35% OR score <65
- Mid-large caps: PLTR, CRWD, NET, MU, AMD

### Tier 3 - Moonshots (20-30%)
- Max position: 4%
- **HARD stop: -40% OR score <50** (NON-NEGOTIABLE)
- Small-mid caps: RKLB, IONQ, HOOD

### Cash (5-10%)
- Dry powder for opportunities
- Deploy into 80+ scores during pullbacks

---

## SCORING QUICK REFERENCE

### What You Enter (Columns E-I)

**Valuation (0-100):**
- Below historical P/E: 85-100
- High FCF yield (>4%): 80-100
- Low PEG (<1.5): 85-100

**Quality (0-100):**
- High ROIC (>25%): 100
- High margins (>30%): 100
- Strong moat (network effects): +20 bonus

**Growth (0-100):**
- Revenue growth >20%: 90-100
- Earnings growth >25%: 100
- Massive TAM with low penetration: +15 bonus

**Momentum (0-100):**
- 12-mo return >40%: 100
- Above 50 & 200-day MA: 100
- Analyst upgrades: +15 bonus

**Financial Health (0-100):**
- Net cash position: 100
- Strong FCF generation: 100

*Use Complete_Scoring_Guide.md for detailed methodology*

---

## MAINTENANCE SCHEDULE

### Weekly (15 min - Monday AM)
- Update prices (or refresh if using Stock data types)
- Update momentum scores
- **Check Tier 3 stop losses** (RED CELLS = ACTION)
- Review Dashboard action items

### Monthly (1 hour - First weekend)
- Update all component scores
- Rebalance positions >2% off target
- Review earnings releases
- Check for exits (score <65 threshold)

### Quarterly (3 hours - After earnings)
- Full review, rescore everything
- Major rebalancing to targets
- Assess tier reclassifications
- Update weights if strategy evolved

---

## WHEN SHIT HITS THE FAN

### Individual Position Crisis

**Stop loss hit:**
→ Sell immediately. No exceptions. Period.

**Score drops >15 points suddenly:**
→ Review thesis. If broken, exit.

**Negative surprise (guidance cut, investigation):**
→ Rescore immediately. Act on signal.

### Portfolio-Wide Crisis

**Down 20%:**
- Move 10% from Tier 3 → Cash
- Tighten Tier 3 stops to -30%

**Down 30%:**
- Move 5% from Tier 2 → Cash
- Raise cash to 15-20%
- Only hold highest conviction

**Down 40%:**
- Exit all positions <65 score
- Preserve capital
- Wait for recovery with cash ready

---

## SUCCESS METRICS

### After 1 Month
✓ All positions scored and entered
✓ Comfortable with weekly routine
✓ Executed first stop loss (hardest part)
✓ Trust in calculations established

### After 1 Quarter
✓ Portfolio outperforming old approach
✓ Less emotional about positions
✓ System refined to personal style
✓ Scoring is intuitive (15 min/stock)

### After 1 Year
✓ Beating QQQ consistently
✓ Sharpe ratio >1.0
✓ System is second nature
✓ Building legacy wealth systematically

---

## EXCEL vs GOOGLE SHEETS: KEY DIFFERENCES

| Feature | Google Sheets | Excel Equivalent |
|---------|---------------|------------------|
| ARRAYFORMULA | `=ARRAYFORMULA(formula)` | Use Excel Tables OR Dynamic Arrays (365) OR fill-down |
| Auto-expand formulas | ARRAYFORMULA | Excel Tables with structured references |
| FILTER function | `=FILTER(range, condition)` | Excel 365: Same / Older: SUMIF, COUNTIF workarounds |
| Named ranges | Data → Named ranges | Formulas → Define Name |
| Protection | Tools → Protect sheet | Review → Protect Sheet |
| Conditional Formatting | Format → Conditional formatting | Home → Conditional Formatting |
| Stock prices | =GOOGLEFINANCE() | Data → Stocks (365) OR manual entry |

---

## FINAL THOUGHTS

**This is your edge:** A systematic framework that removes emotion from investing.

**The discipline:** Stop losses on Tier 3 are non-negotiable. This protects capital for next opportunities.

**The payoff:** Years of compound growth through calculated aggressive investing.

**The philosophy:** You're not gambling. You're restoring order to chaos. Every position has a quantified score. Every action has a trigger. Every risk has a boundary.

**Your style:** Data-backed intuition. Trust the process you built.

---

## NEXT ACTION

**Right now:**
1. Open Excel (Desktop or Excel 365)
2. Follow Phase 1-7 in order
3. 2-3 hours later, you have a bulletproof system

**This week:**
- Enter your positions
- Score them properly
- Watch it work

**This month:**
- Execute the process
- Build the habit
- Trust the system

**This year:**
- Outperform
- Compound
- Build legacy

---

**The market rewards discipline.**
**This system IS your discipline.**

**Now go build it.** 💪📈

---

**Version: Excel Direct Action**
**Created: October 2025**
**Excel Compatible: 2016, 2019, Excel 365**
**Time: 2-3 hours to bulletproof wealth**
