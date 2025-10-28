# QUICK START: Import Stock Rating Sheet in 5 Minutes

## Option 1: Import CSV (Fastest Method)

### Step 1: Get the CSV File
Download `stock_rating_template.csv` from this repository

### Step 2: Import to Google Sheets
1. Go to [Google Sheets](https://sheets.google.com)
2. Click **File → Import**
3. Click **Upload** tab
4. Drag and drop `stock_rating_template.csv` or click **Browse**
5. In Import settings:
   - **Import location:** Replace spreadsheet
   - **Separator type:** Detect automatically (should be Comma)
   - **Convert text to numbers, dates, and formulas:** ✅ **YES** (Very important!)
6. Click **Import data**

### Step 3: Verify Formulas Loaded
1. Click on cell **E2** - should show formula: `=IF(D2>300,"Tier 1",IF(D2>=20,"Tier 2","Tier 3"))`
2. Click on cell **AF2** - should show a long formula starting with `=IF(E2="Tier 1"...`
3. If you see formulas, you're good! If you see text, re-import with "Convert text to formulas" checked

### Step 4: Apply Formatting (5 minutes)

#### A. Format Headers (Row 1)
1. Select Row 1
2. **Bold** + **Center align** + **Background: Light gray**

#### B. Color Input Columns (Blue)
1. Select columns **A-D, F-Z** (skip E which is calculated)
2. Text color: **Blue (#0000FF)**

#### C. Color Calculated Columns (Black Bold)
1. Select columns **E, AA-AH**
2. Text color: **Black (#000000)**
3. Font weight: **Bold**

#### D. Add Score Color Scales
1. Select **AA2:AE30** (all score columns)
2. **Format → Conditional formatting**
3. Format rules:
   - **Color scale**
   - Min value (0): **Red**
   - Midpoint (50): **Yellow**
   - Max value (100): **Green**
4. Click **Done**

#### E. Highlight Composite Scores
1. Select **AF2:AF30**
2. **Format → Conditional formatting** → Add rule
3. Format cells if... **Greater than or equal to** `85`
   - Background: **Dark Green (#00FF00)**, Text: **White**
4. Add more rules:
   - `>= 75`: Light Green background
   - `>= 65`: Yellow background
   - `>= 55`: Orange background
   - `< 55`: Red background, White text

#### F. Color Action Signals
1. Select **AH2:AH30**
2. **Format → Conditional formatting**
3. Add rules for "Text contains":
   - **ADD**: Dark Green background, White text
   - **BUY**: Light Green background
   - **HOLD**: Yellow background
   - **EXIT**: Red background, White text

### Step 5: Test the System
Your imported sheet should already have 3 example stocks:
- **GOOGL** (Row 2) - Should show Tier 1, score ~82
- **PLTR** (Row 3) - Should show Tier 2, score ~86
- **RKLB** (Row 4) - Should show Tier 3, score ~78

### Step 6: Add Your First Stock
1. Go to Row 5 (first empty row after examples)
2. Enter data for a stock you own
3. Watch the scores auto-calculate!

---

## Option 2: Manual Setup (From Scratch)

If you prefer to build it yourself, follow the detailed instructions in `GOOGLE_SHEETS_IMPLEMENTATION.md`

---

## Troubleshooting Import Issues

### Issue: Formulas appear as text
**Solution:**
1. Delete the sheet
2. Re-import CSV
3. **Make sure** "Convert text to numbers, dates, and formulas" is **CHECKED**

### Issue: Scores show #DIV/0!
**Solution:**
- This is normal for empty rows
- Fill in data and they'll calculate

### Issue: Formulas reference wrong rows
**Solution:**
- The CSV has formulas for rows 2-4
- To add more rows, copy row 4 and paste to rows 5-30

### Issue: CSV won't upload
**Solution:**
- Make sure file extension is `.csv`
- Try opening in text editor to verify it's valid CSV
- Max file size for Google Sheets: 5MB (this is <1MB)

---

## Next Steps After Import

1. **Delete example stocks** (rows 2-4) or keep as reference
2. **Add your portfolio** starting at row 2 or 5
3. **Copy formulas down** to row 30 (for 25+ stock capacity)
4. **Set up data validation** for Y/N columns (see main guide)
5. **Freeze header row** (View → Freeze → 1 row)
6. **Share or keep private** (File → Share)

---

## Expanding Capacity

The template includes 3 example stocks. To add more:

1. Select row 4 (RKLB row)
2. Copy entire row (Ctrl+C)
3. Select rows 5-30
4. Paste (Ctrl+V)
5. Clear the data in columns A-D, F-Z (keep formulas in E, AA-AH)
6. Now you have space for 25+ stocks!

---

## Quick Reference: What to Enter Where

**Must fill for all stocks:**
- **A-D:** Ticker, Company, Price, Market Cap
- **L-M:** Revenue Growth %, EPS Growth %
- **N:** Operating Margin %
- **V:** 12-month return %
- **W:** Above 200MA? (Y/N)

**Should fill when available:**
- **F:** Beta
- **H-I:** Forward P/E, 5yr Avg P/E (for profitable companies)
- **J:** Free Cash Flow
- **K:** P/S Ratio (for unprofitable companies)
- **P:** ROIC %
- **Q:** Gross Margin %
- **X:** Net Cash
- **Z:** Has Moat? (Y/N)

**Nice to have:**
- **O:** Op Margin 3yr Average
- **R:** NRR % (for SaaS only)
- **S:** Cash Conversion
- **T-U:** TAM and TAM Penetration %
- **Y:** Insider Ownership %

---

## Success Check ✅

After import, verify:
- [ ] 3 example stocks visible (GOOGL, PLTR, RKLB)
- [ ] Column E shows "Tier 1", "Tier 2", "Tier 3"
- [ ] Columns AA-AE show numbers (scores)
- [ ] Column AF shows composite scores (70-90 range for examples)
- [ ] Column AG shows star ratings
- [ ] Column AH shows actions (ADD, BUY, etc.)
- [ ] Headers are in row 1
- [ ] No #REF! or #NAME? errors

If all checked, **you're ready to use the system!** 🚀

---

## Support

**Full Documentation:** See `GOOGLE_SHEETS_IMPLEMENTATION.md`
**User Guide:** See `SINGLE_SHEET_STOCK_RATING_USER_GUIDE.md`
**Formula Reference:** See implementation guide

**Questions?** Check the Troubleshooting sections in the main guides.
