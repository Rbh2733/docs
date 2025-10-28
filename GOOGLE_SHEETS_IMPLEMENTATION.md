# SINGLE-SHEET STOCK RATING SYSTEM - GOOGLE SHEETS IMPLEMENTATION

## Quick Setup Guide

### Step 1: Create New Google Sheet
1. Go to [Google Sheets](https://sheets.google.com)
2. Create a new blank spreadsheet
3. Name it: "Single Sheet Stock Rating System"

### Step 2: Set Up Headers

Copy these headers into Row 1:

| Col | Header | Type | Col | Header | Type |
|-----|--------|------|-----|--------|------|
| A | Ticker | INPUT | U | TAM Penetration % | INPUT |
| B | Company | INPUT | V | 12mo Return % | INPUT |
| C | Price | INPUT | W | Above 200MA? | INPUT |
| D | Market Cap ($B) | INPUT | X | Net Cash ($B) | INPUT |
| E | Tier | CALC | Y | Insider Own % | INPUT |
| F | Beta | INPUT | Z | Has Moat? | INPUT |
| G | Sector | INPUT | AA | Valuation Score | CALC |
| H | Forward P/E | INPUT | AB | Quality Score | CALC |
| I | 5yr Avg P/E | INPUT | AC | Growth Score | CALC |
| J | FCF ($B) | INPUT | AD | Momentum Score | CALC |
| K | P/S Ratio | INPUT | AE | Financial Health | CALC |
| L | Revenue Growth % | INPUT | AF | Composite Score | CALC |
| M | EPS Growth % | INPUT | AG | Rating | CALC |
| N | Operating Margin % | INPUT | AH | Action | CALC |
| O | Op Margin 3yr Avg % | INPUT | | | |
| P | ROIC % | INPUT | | | |
| Q | Gross Margin % | INPUT | | | |
| R | NRR % | INPUT | | | |
| S | Cash Conversion | INPUT | | | |
| T | TAM ($B) | INPUT | | | |

---

## FORMULAS - Copy into Row 2 (First Stock)

### Column E: Tier Classification
```
=IF(D2>300,"Tier 1",IF(D2>=20,"Tier 2","Tier 3"))
```

### Column AA: Valuation Score (0-100)
```
=IF(E2="Tier 1",
  MIN(100,
    IF(H2>0,35*MIN(100,MAX(0,100*(1-(H2-I2)/I2))),0) +
    IF(J2>0,30*MIN(100,(J2/D2)*10*100),0) +
    IF(AND(H2>0,L2>0),35*MIN(100,100*(1/MAX(0.5,(H2/L2)))),0)
  ),
  IF(E2="Tier 2",
    MIN(100,
      IF(H2>0,25*MIN(100,MAX(0,100*(1-(H2-I2)/I2))),0) +
      IF(K2>0,30*MIN(100,MAX(0,100*(1-K2/15))),15*IF(J2>0,MIN(100,(J2/D2)*10*100),0)) +
      IF(AND(H2>0,L2>0),25*MIN(100,100*(1/MAX(0.5,(H2/L2)))),0) +
      IF(Y2>5,20,IF(Y2>2,10,0))
    ),
    IF(E2="Tier 3",
      MIN(100,
        IF(K2>0,50*MIN(100,MAX(0,100*(1-K2/20))),0) +
        IF(Y2>10,30,IF(Y2>5,20,IF(Y2>2,10,0))) +
        20*IF(L2>50,100,IF(L2>30,80,IF(L2>20,60,40)))
      ),
    0)
  )
)
```

### Column AB: Quality Score (0-100)
```
=IF(E2="Tier 1",
  MIN(100,
    IF(P2>=25,25,IF(P2>=15,20,IF(P2>=10,15,P2))) +
    IF(N2>=30,25,IF(N2>=20,20,IF(N2>=15,15,N2*0.5))) +
    IF(N2>O2,10,IF(N2>O2*0.95,5,0)) +
    IF(Z2="Y",20,0) +
    IF(S2>1.2,20,IF(S2>1,15,IF(S2>0.8,10,S2*10)))
  ),
  IF(E2="Tier 2",
    MIN(100,
      IF(P2>=20,20,IF(P2>=12,15,IF(P2>=8,10,P2*0.8))) +
      IF(N2>=25,20,IF(N2>=15,15,IF(N2>=10,10,N2*0.5))) +
      IF(Q2>=75,25,IF(Q2>=65,20,IF(Q2>=55,15,Q2*0.2))) +
      IF(R2>0,MIN(20,R2/7),0) +
      IF(Z2="Y",15,0)
    ),
    IF(E2="Tier 3",
      MIN(100,
        IF(Q2>=70,40,IF(Q2>=60,30,IF(Q2>=50,20,Q2*0.3))) +
        IF(N2>0,20,IF(N2>-10,15,IF(N2>-20,10,0))) +
        IF(P2>0,20,IF(P2>-5,15,IF(P2>-15,10,0))) +
        IF(Z2="Y",20,0)
      ),
    0)
  )
)
```

### Column AC: Growth Score (0-100)
```
=IF(E2="Tier 1",
  MIN(100,
    IF(L2>=20,40,IF(L2>=15,35,IF(L2>=10,25,L2*2))) +
    IF(M2>=25,35,IF(M2>=15,25,IF(M2>=10,20,M2*1.5))) +
    IF(U2>0,25*MIN(100,(100-U2)/100),15)
  ),
  IF(E2="Tier 2",
    MIN(100,
      IF(L2>=40,45,IF(L2>=30,40,IF(L2>=20,30,L2*1.2))) +
      IF(M2>=30,35,IF(M2>=20,28,IF(M2>=15,20,M2*1))) +
      IF(U2>0,20*MIN(100,(100-U2)/100),10)
    ),
    IF(E2="Tier 3",
      MIN(100,
        IF(L2>=100,50,IF(L2>=75,45,IF(L2>=50,40,L2*0.6))) +
        IF(U2<5,30,IF(U2<10,25,IF(U2<20,20,15))) +
        IF(T2>500,20,IF(T2>200,15,IF(T2>50,10,5)))
      ),
    0)
  )
)
```

### Column AD: Momentum Score (0-100)
```
=MIN(100,
  IF(V2>=100,45,IF(V2>=50,40,IF(V2>=25,35,IF(V2>=0,30,IF(V2>=-20,20,10))))) +
  IF(W2="Y",30,0) +
  IF(V2>0,25*MIN(100,V2/100),0)
)
```

### Column AE: Financial Health Score (0-100)
```
=IF(E2="Tier 1",
  MIN(100,
    IF(X2>50,40,IF(X2>25,35,IF(X2>0,25,IF(X2>-25,15,5)))) +
    IF(J2>10,40,IF(J2>5,30,IF(J2>2,20,IF(J2>0,10,0)))) +
    IF(S2>1.2,20,IF(S2>1,15,IF(S2>0.8,10,0)))
  ),
  IF(E2="Tier 2",
    MIN(100,
      IF(X2>25,35,IF(X2>10,30,IF(X2>0,25,IF(X2>-10,15,5)))) +
      IF(J2>5,40,IF(J2>2,30,IF(J2>1,20,IF(J2>0,10,0)))) +
      IF(S2>1,25,IF(S2>0.8,20,IF(S2>0.5,15,10)))
    ),
    IF(E2="Tier 3",
      MIN(100,
        IF(X2>5,30,IF(X2>0,25,IF(X2>-5,20,IF(X2>-15,15,10)))) +
        IF(J2>1,35,IF(J2>0.5,25,IF(J2>0,15,IF(J2>-1,10,5)))) +
        IF(L2>75,35,IF(L2>50,25,IF(L2>30,15,10)))
      ),
    0)
  )
)
```

### Column AF: Composite Score (Weighted Average)
```
=IF(E2="Tier 1",
  ROUND(
    AA2*0.20 +
    AB2*0.30 +
    AC2*0.30 +
    AD2*0.10 +
    AE2*0.10,
  0),
  IF(E2="Tier 2",
    ROUND(
      AA2*0.18 +
      AB2*0.25 +
      AC2*0.35 +
      AD2*0.12 +
      AE2*0.10,
    0),
    IF(E2="Tier 3",
      ROUND(
        AA2*0.15 +
        AB2*0.15 +
        AC2*0.45 +
        AD2*0.20 +
        AE2*0.05,
      0),
    0)
  )
)
```

### Column AG: Rating (Star System)
```
=IF(E2="Tier 1",
  IF(AF2>=85,"★★★★★ Strong Buy",
    IF(AF2>=75,"★★★★ Buy",
      IF(AF2>=65,"★★★ Hold",
        IF(AF2>=55,"★★ Reduce","★ Exit")))),
  IF(E2="Tier 2",
    IF(AF2>=85,"★★★★★ Strong Buy",
      IF(AF2>=75,"★★★★ Buy",
        IF(AF2>=65,"★★★ Accumulate",
          IF(AF2>=55,"★★ Hold","★ Exit")))),
    IF(E2="Tier 3",
      IF(AF2>=80,"★★★★★ Strong Buy",
        IF(AF2>=70,"★★★★ Buy",
          IF(AF2>=65,"★★★ Speculative Buy",
            IF(AF2>=60,"★★ Watch","★ Pass")))),
    "")))
```

### Column AH: Action Signal
```
=IF(E2="Tier 1",
  IF(AF2>=75,"ADD",IF(AF2>=65,"HOLD",IF(AF2>=55,"REDUCE","EXIT"))),
  IF(E2="Tier 2",
    IF(AF2>=75,"ADD",IF(AF2>=65,"ACCUMULATE",IF(AF2>=55,"HOLD","EXIT"))),
    IF(E2="Tier 3",
      IF(AF2>=70,"ADD",IF(AF2>=65,"BUY",IF(AF2>=60,"WATCH","PASS"))),
    "")))
```

---

## EXAMPLE DATA - Row 2 (GOOGL - Tier 1)

Copy this into Row 2 to test:

| A | B | C | D | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| GOOGL | Alphabet Inc | 140 | 1800 | 1.1 | Technology | 22 | 25 | 70 | 5 | 13 | 22 | 32 | 30 | 28 | 57 | | 1.3 | 2000 | 4 | 45 | Y | 100 | 2 | Y |

---

## EXAMPLE DATA - Row 3 (PLTR - Tier 2)

| A | B | C | D | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| PLTR | Palantir | 28 | 60 | 2.3 | Software | 50 | 45 | 1.2 | 12 | 30 | 35 | 18 | 15 | 15 | 78 | 120 | 1.4 | 450 | 3 | 68 | Y | 4 | 8 | Y |

---

## EXAMPLE DATA - Row 4 (RKLB - Tier 3)

| A | B | C | D | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RKLB | Rocket Lab | 12 | 6 | 2.8 | Aerospace | | | -0.3 | 25 | 85 | | -15 | -20 | -10 | 68 | | -2 | 180 | 1 | 110 | Y | 0.5 | 12 | Y |

---

## CONDITIONAL FORMATTING SETUP

### Format Input Columns (Blue Text)
1. Select columns A-D, F-Z
2. Format → Text color → Blue (#0000FF)
3. Format → Font weight → Normal

### Format Calculated Columns (Black Text)
1. Select columns E, AA-AH
2. Format → Text color → Black (#000000)
3. Format → Font weight → Bold

### Color Scale for Scores (AA-AF)
1. Select range AA2:AE25 (or your data range)
2. Format → Conditional formatting
3. Color scale:
   - Minimum (0): Red (#FF0000)
   - Midpoint (50): Yellow (#FFFF00)
   - Maximum (100): Green (#00FF00)

### Composite Score Highlighting (AF)
1. Select AF2:AF25
2. Format → Conditional formatting
3. Add rules:
   - >= 85: Dark Green background, White text
   - >= 75: Light Green background, Black text
   - >= 65: Yellow background, Black text
   - >= 55: Orange background, Black text
   - < 55: Red background, White text

### Action Signal Colors (AH)
1. Select AH2:AH25
2. Format → Conditional formatting
3. Text contains rules:
   - "ADD": Dark Green background, White text
   - "BUY": Light Green background, Black text
   - "ACCUMULATE": Light Blue background, Black text
   - "HOLD": Yellow background, Black text
   - "REDUCE": Orange background, Black text
   - "EXIT": Red background, White text
   - "PASS": Light Red background, Black text

---

## DATA VALIDATION (Optional but Recommended)

### Above 200MA (Column W)
1. Select W2:W25
2. Data → Data validation
3. Criteria: List of items: Y,N
4. On invalid data: Reject input

### Has Moat (Column Z)
1. Select Z2:Z25
2. Data → Data validation
3. Criteria: List of items: Y,N
4. On invalid data: Reject input

---

## FREEZING AND LAYOUT

### Freeze Header Row
1. Click on Row 2
2. View → Freeze → 1 row

### Adjust Column Widths
- A (Ticker): 80px
- B (Company): 150px
- C-Z: 100px
- AA-AE (Scores): 110px
- AF (Composite): 120px
- AG (Rating): 180px
- AH (Action): 100px

---

## FINAL CHECKLIST

- [ ] All headers in Row 1
- [ ] Formulas in columns E, AA-AH starting Row 2
- [ ] Example data (GOOGL, PLTR, RKLB) in rows 2-4
- [ ] Conditional formatting applied
- [ ] Input columns colored blue
- [ ] Calculated columns colored black/bold
- [ ] Data validation on Y/N columns
- [ ] Header row frozen
- [ ] Column widths adjusted
- [ ] Formula copied down to Row 25 (for 20+ stocks capacity)

---

## USAGE TIPS

### Adding New Stocks
1. Find next empty row
2. Enter ticker, company name, and all INPUT data (blue columns)
3. Formulas auto-calculate if you've copied them down
4. Review composite score and action signal

### Copying Formulas Down
1. Select Row 2 (E2, AA2:AH2)
2. Copy (Ctrl+C)
3. Select E3:E25, AA3:AH25
4. Paste (Ctrl+V)

### Updating Data
- **Weekly**: Update columns C, V, W
- **Monthly**: Update all data after earnings
- **Quarterly**: Full refresh of all inputs

---

## TROUBLESHOOTING

### #DIV/0! Error
- Check that Market Cap (D) has a value
- Ensure growth rates aren't causing division by zero
- Verify TAM (T) is filled in

### #VALUE! Error
- Make sure percentages are entered as numbers (12, not "12%")
- Check Y/N columns have exactly "Y" or "N"
- Verify all number fields contain numbers, not text

### Score Seems Wrong
1. Check tier classification (column E)
2. Verify all inputs are in correct units ($B not $M)
3. Review each component score (AA-AE) to see which is off
4. Ensure percentages are whole numbers (30 not 0.30)

---

## SHARING & COLLABORATION

### Making Shareable
1. File → Share
2. Set to "Anyone with link can view"
3. For collaborators who will add data: "Can edit"

### Protection (Recommended)
1. Protect calculated columns from accidental edits:
2. Select columns E, AA-AH
3. Data → Protect sheet
4. Set permissions: "Show a warning"

---

## NEXT STEPS

1. ✅ Create the sheet with headers
2. ✅ Copy all formulas into Row 2
3. ✅ Add example data to test
4. ✅ Apply conditional formatting
5. ✅ Copy formulas down to Row 25
6. 📊 Start scoring your portfolio!

---

**Created:** October 2025
**System Version:** 1.0
**Compatible with:** Google Sheets, Excel 2016+, LibreOffice Calc
