# Verification Checklist - Amazon Web Scraping Project

---

## Document Information

| Property | Value |
|----------|-------|
| **Version** | 1.0.0 |
| **Last Updated** | 2026-07-21 |
| **Status** | Ready for Verification |
| **Total Checks** | 85 |

---

## Reference Documentation

| Document | Purpose |
|----------|---------|
| [Technical Blueprint](blueprint.md) | Technical specifications and architecture |
| [README](../README.md) | Project overview and quick start |
| [Cheat Sheet](cheatsheets.md) | Quick commands reference |

---

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ⬜ | Pending / Not yet started |
| ✅ | Complete / Passed |
| 🔄 | In Progress |
| ❌ | Failed / Needs attention |
| ⚠️ | Warning / Needs review |

---

## Phase 1: Setup & Environment

**Phase Goal:** All project files and environment configured correctly

| # | Task | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 1.1 | Project folder structure created | README | ✅ | Amazon-Web-Scrapping/ with all subfolders |
| 1.2 | Virtual environment created | blueprint.md#deployment | ✅ | python -m venv venv |
| 1.3 | Virtual environment activated | blueprint.md#deployment | ✅ | (venv) active |
| 1.4 | requirements.txt created | blueprint.md#deployment | ✅ | All dependencies listed |
| 1.5 | All dependencies installed | blueprint.md#deployment | ✅ | pip install -r requirements.txt |
| 1.6 | Jupyter Notebook installed | blueprint.md#deployment | ✅ | jupyter --version |
| 1.7 | Git initialized | - | ✅ | git init |
| 1.8 | .gitignore configured | - | ✅ | Python + Jupyter |

**Phase 1 Checks:** 8 | **Passed:** 8 | **Failed:** 0 | **Pending:** 0 | **Progress:** 100%

---

## Phase 2: Jupyter Notebook Setup

**Phase Goal:** All notebook files properly configured

| # | Task | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 2.1 | `amazon_web_scraping_tutorial.ipynb` exists | README | ✅ | Main tutorial notebook |
| 2.2 | `amazon_scrape_final.ipynb` exists | README | ✅ | Final scraper version |
| 2.3 | Notebooks open without errors | blueprint.md | ✅ | No kernel errors |
| 2.4 | All imports working | blueprint.md#implementation | ✅ | bs4, requests, pandas, numpy |
| 2.5 | Notebook can execute cells | - | ✅ | Run all cells successfully |

**Phase 2 Checks:** 5 | **Passed:** 5 | **Failed:** 0 | **Pending:** 0 | **Progress:** 100%

---

## Phase 3: Code Implementation Verification

**Phase Goal:** All functions properly implemented

| # | Task | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 3.1 | `get_title()` function defined | blueprint.md#implementation | ✅ | Extract product title |
| 3.2 | `get_price()` function defined | blueprint.md#implementation | ✅ | Extract product price |
| 3.3 | `get_rating()` function defined | blueprint.md#implementation | ✅ | Extract product rating |
| 3.4 | `get_review_count()` function defined | blueprint.md#implementation | ✅ | Extract review count |
| 3.5 | `get_availability()` function defined | blueprint.md#implementation | ✅ | Extract availability status |
| 3.6 | Each function handles AttributeError | blueprint.md#implementation | ✅ | Try-except blocks present |
| 3.7 | HEADERS with User-Agent configured | blueprint.md#implementation | ✅ | Browser-like headers |
| 3.8 | Search URL properly formatted | blueprint.md#implementation | ✅ | `https://www.amazon.com/s?k=playstation+5` |
| 3.9 | Product links extraction logic present | blueprint.md#implementation | ✅ | `soup.find_all('a', class_='a-link-normal s-no-outline')` |
| 3.10 | Data dictionary initialized with 5 keys | blueprint.md#implementation | ✅ | `{"title": [], "price": [], ...}` |
| 3.11 | Loop through links to scrape each product | blueprint.md#implementation | ✅ | `for link in links_list:` |
| 3.12 | DataFrame creation from dictionary | blueprint.md#implementation | ✅ | `pd.DataFrame.from_dict(d)` |
| 3.13 | Empty titles replaced with NaN | blueprint.md#implementation | ✅ | `df['title'].replace('', np.nan, inplace=True)` |
| 3.14 | Rows with empty titles dropped | blueprint.md#implementation | ✅ | `df.dropna(subset=['title'])` |
| 3.15 | CSV export with proper parameters | blueprint.md#implementation | ✅ | `to_csv("amazon_data.csv", header=True, index=False)` |

**Phase 3 Checks:** 15 | **Passed:** 15 | **Failed:** 0 | **Pending:** 0 | **Progress:** 100%

---

## Phase 4: Scraping Execution Test

**Phase Goal:** Pipeline executes successfully without errors

| # | Task | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 4.1 | Search request returns status_code=200 | blueprint.md#data-flow | ✅ | HTTP request successful |
| 4.2 | Product links extracted successfully | blueprint.md#data-flow | ✅ | links_list not empty |
| 4.3 | Each product page loads successfully | blueprint.md#data-flow | ✅ | No 404 errors |
| 4.4 | Titles extracted successfully | blueprint.md#implementation | ✅ | Title values present |
| 4.5 | Prices extracted for available products | blueprint.md#implementation | ⚠️ | Price values may be N/A for discontinued products |
| 4.6 | Ratings extracted for rated products | blueprint.md#implementation | ✅ | Rating values present |
| 4.7 | Review counts extracted for products with reviews | blueprint.md#implementation | ✅ | Review count values present |
| 4.8 | Availability extracted successfully | blueprint.md#implementation | ✅ | Availability values present |
| 4.9 | No AttributeError exceptions during scraping | blueprint.md#implementation | ✅ | All try-except working |
| 4.10 | Data dictionary populated | blueprint.md#implementation | ✅ | All lists have data |
| 4.11 | DataFrame created successfully | blueprint.md#implementation | ✅ | pd.DataFrame.from_dict(d) |
| 4.12 | DataFrame has expected columns | blueprint.md#data-model | ✅ | title, price, rating, reviews, availability |
| 4.13 | Empty rows removed properly | blueprint.md#implementation | ✅ | dropna(subset=['title']) |
| 4.14 | CSV file generated | blueprint.md#implementation | ✅ | amazon_data.csv exists |
| 4.15 | CSV has header row | blueprint.md#implementation | ✅ | header=True |
| 4.16 | CSV has data rows | blueprint.md#implementation | ✅ | At least 1 row of data |
| 4.17 | Scraping completes without errors | blueprint.md#implementation | ✅ | No exceptions during execution |
| 4.18 | Execution time < 60 seconds (for 10+ products) | blueprint.md#performance | ✅ | Reasonable scraping speed |

**Phase 4 Checks:** 18 | **Passed:** 17 | **Failed:** 0 | **Pending:** 0 | **Progress:** 94.44%

---

## Phase 5: Data Quality Verification

**Phase Goal:** Scraped data is clean and properly structured

| # | Task | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 5.1 | CSV file readable | blueprint.md | ✅ | pd.read_csv('amazon_data.csv') |
| 5.2 | CSV has 5 columns | blueprint.md#data-model | ✅ | title, price, rating, reviews, availability |
| 5.3 | No rows with empty titles | blueprint.md#implementation | ✅ | All titles have values |
| 5.4 | Title values are strings | blueprint.md#data-model | ✅ | String type |
| 5.5 | Price values include $ symbol | blueprint.md#data-model | ⚠️ | Some prices may be N/A for discontinued products |
| 5.6 | Rating values contain "out of 5 stars" | blueprint.md#data-model | ✅ | Rating format preserved |
| 5.7 | Review values contain "ratings" | blueprint.md#data-model | ✅ | Review format preserved |
| 5.8 | Availability values present | blueprint.md#data-model | ✅ | Availability values present |
| 5.9 | No duplicate products (same title) | - | ✅ | Check for duplicates |
| 5.10 | Data types are consistent | - | ✅ | All rows have same types |

**Phase 5 Checks:** 10 | **Passed:** 8 | **Failed:** 0 | **Pending:** 0 | **Progress:** 80%

---

## Phase 6: Screenshots Documentation

**Phase Goal:** All screenshots captured and saved

| # | Filename | Description | Reference | Status |
|---|----------|-------------|-----------|--------|
| 6.1 | `folder_structure.png` | Project folder structure in VS Code | images/ | ✅ |
| 6.2 | `scraping_result_Jupyter.png` | Scraping results in Jupyter Notebook | images/ | ✅ |
| 6.3 | `csv_output_excel.png` | CSV output opened in Excel | images/ | ✅ |
| 6.4 | `architecture-diagram.png` | System architecture diagram | images/ | ✅ |
| 6.5 | `Function to extract Product Title.png` | Title extraction function in notebook | images/ | ✅ |
| 6.6 | `Function to extract Product Price.png` | Price extraction function in notebook | images/ | ✅ |
| 6.7 | `Function to extract Product Rating.png` | Rating extraction function in notebook | images/ | ✅ |
| 6.8 | `Function to extract Number of User Reviews.png` | Review count extraction function in notebook | images/ | ✅ |
| 6.9 | `Function to extract Availability Status.png` | Availability extraction function in notebook | images/ | ✅ |

**Phase 6 Checks:** 9 | **Passed:** 9 | **Failed:** 0 | **Pending:** 0 | **Progress:** 100%

---

## Phase 7: Documentation & Deployment

**Phase Goal:** All documentation complete and project deployed

| # | Task | Reference | Status | Notes |
|---|------|-----------|--------|-------|
| 7.1 | README.md completed | README | ✅ | Full documentation |
| 7.2 | blueprint.md completed | blueprint.md | ✅ | Technical blueprint |
| 7.3 | verification checklist.md completed | This file | ✅ | Testing checklist |
| 7.4 | cheatsheet.md completed | cheatsheet.md | ✅ | Quick reference |
| 7.5 | CHANGELOG.md completed | CHANGELOG.md | ✅ | Version history |
| 7.6 | CONTRIBUTING.md completed | CONTRIBUTING.md | ✅ | Contribution guidelines |
| 7.7 | LICENSE added | - | ✅ | MIT License |
| 7.8 | .gitignore configured | - | ✅ | Python + Jupyter |
| 7.9 | Git commit | - | ✅ | All files committed |
| 7.10 | GitHub repository created | - | ✅ | Public repo |
| 7.11 | Remote origin set | - | ✅ | git remote add origin |
| 7.12 | Push to GitHub | - | ✅ | git push -u origin main |
| 7.13 | README rendered on GitHub | - | ✅ | Check formatting |
| 7.14 | Screenshots visible on GitHub | - | ✅ | Images render |

**Phase 7 Checks:** 14 | **Passed:** 14 | **Failed:** 0 | **Pending:** 0 | **Progress:** 100%

---

## Overall Summary

| Phase | Total Checks | Passed | Failed | Pending | Progress |
|-------|--------------|--------|--------|---------|----------|
| Phase 1: Setup & Environment | 8 | 8 | 0 | 0 | 100% |
| Phase 2: Jupyter Notebook Setup | 5 | 5 | 0 | 0 | 100% |
| Phase 3: Code Implementation Verification | 15 | 15 | 0 | 0 | 100% |
| Phase 4: Scraping Execution Test | 18 | 17 | 0 | 0 | 94.44% |
| Phase 5: Data Quality Verification | 10 | 8 | 0 | 0 | 80% |
| Phase 6: Screenshots Documentation | 9 | 9 | 0 | 0 | 100% |
| Phase 7: Documentation & Deployment | 14 | 14 | 0 | 0 | 100% |
| **TOTAL** | **79** | **76** | **0** | **0** | **96.20% Complete** |

---

## Quick Commands Reference

### Run Scraper

```bash
# Open tutorial notebook
jupyter notebook amazon_web_scraping_tutorial.ipynb

# Open final notebook
jupyter notebook amazon_scrape_final.ipynb

# Convert to script and run
jupyter nbconvert --to script amazon_scrape_final.ipynb
python amazon_scrape_final.py

# Run Python script directly
python amazon_scrape_final.py
```

### Verify CSV Output

```python
import pandas as pd
df = pd.read_csv('amazon_data.csv')
print(f"Rows: {len(df)}")
print(f"Columns: {df.columns.tolist()}")
print(df.head())
```

### Check Data Quality

```python
# Check for empty values
print(df.isnull().sum())

# Check data types
print(df.dtypes)

# Check for duplicates
print(f"Duplicates: {df.duplicated().sum()}")
```

---

## Troubleshooting Checklist

### If Scraping Fails

| Issue | Check |
|-------|-------|
| 403 Forbidden | Update User-Agent headers |
| Connection timeout | Check internet connection |
| Empty links_list | Search result structure changed |
| Empty titles | Product page structure changed |
| No CSV generated | Check if code executed completely |
| Price N/A | Product may be discontinued or geo-blocked |

### If Data Quality Issues

| Issue | Check |
|-------|-------|
| Missing values | Check if selectors are correct |
| Wrong data types | Check data cleaning steps |
| Duplicate rows | Add drop_duplicates() |
| Empty CSV | Check if links_list had data |

---

## Completion Checklist

Before finalizing the project, ensure all these items are complete:

### Code
- [x] All 5 extraction functions implemented
- [x] Error handling in place
- [x] CSV export working
- [x] No syntax errors

### Data
- [x] CSV file generated
- [x] Data quality checks passed
- [x] No empty rows

### Documentation
- [x] README.md complete
- [x] blueprint.md complete
- [x] verification checklist.md complete (this file)
- [x] cheatsheet.md complete
- [x] CHANGELOG.md complete
- [x] CONTRIBUTING.md complete

### Screenshots
- [x] 9 screenshots captured
- [x] Screenshots saved in images/
- [x] Screenshots visible in README

### Deployment
- [x] GitHub repository public
- [x] All code pushed
- [x] README rendered correctly

---

**Ready for verification!**

*Last Updated: 2026-07-21*