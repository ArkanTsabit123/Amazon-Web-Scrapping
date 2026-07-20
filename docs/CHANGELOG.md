# Changelog - Amazon Web Scraping Project

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.0.0] - 2026-07-21

### Added
- Initial project setup and repository creation
- `amazon_scrape_final.ipynb` - Final working scraper implementation
- `amazon_web_scraping_tutorial.ipynb` - Step-by-step tutorial notebook
- `amazon_scrape_final.py` - Python script version of the scraper
- Working scraper with product data extraction from Amazon search results
- 5 extraction functions:
  - `get_title()` - Extract product title from `#productTitle`
  - `get_price()` - Extract product price from `#priceblock_ourprice` or `#priceblock_dealprice`
  - `get_rating()` - Extract product rating from `.a-icon-star` or `.a-icon-alt`
  - `get_review_count()` - Extract review count from `#acrCustomerReviewText`
  - `get_availability()` - Extract availability from `#availability`
- HTTP request configuration with custom User-Agent headers
- Random User-Agent rotation for anti-detection
- Search result scraping from Amazon with `playstation 5` keyword
- Data cleaning pipeline using Pandas
- CSV export functionality (`amazon_data.csv`)
- Multi-product scraping with 10 popular keywords
- `amazon_all_products.csv` - Combined CSV output for multi-product scraping
- Filter for "Renewed" and "Used" products
- Error handling with try-except blocks
- Random delays between requests (2-4 seconds)
- Project documentation:
  - `README.md` - Project overview and quick start guide
  - `docs/blueprint.md` - Technical blueprint
  - `docs/cheatsheets.md` - Quick reference commands
  - `docs/verification_checklist.md` - Testing checklist with 85 checks
  - `CHANGELOG.md` - Version history
  - `CONTRIBUTING.md` - Contribution guidelines
- Screenshots documentation (9 images):
  - `images/folder_structure.png` - Project folder structure
  - `images/scraping_result_Jupyter.png` - Scraping results in Jupyter
  - `images/csv_output_excel.png` - CSV output in Excel
  - `images/architecture-diagram.png` - System architecture diagram
  - `images/Function to extract Product Title.png`
  - `images/Function to extract Product Price.png`
  - `images/Function to extract Product Rating.png`
  - `images/Function to extract Number of User Reviews.png`
  - `images/Function to extract Availability Status.png`
- `.gitignore` for Python and Jupyter Notebook files
- `requirements.txt` with all dependencies
- `LICENSE` - MIT License
- Jupyter Notebook checkpoint file handling

### Changed
- Updated default search keyword from "playstation 4" to "playstation 5"
- Improved extraction functions with multiple selector fallbacks
- Enhanced price extraction with `.a-price .a-offscreen` selector
- Refactored code structure for better maintainability (PEP 8 compliant)
- Improved filter logic to exclude "Renewed" and "Used" products
- Simplified README with clear project structure and concise description

### Fixed
- Price extraction failure due to outdated selectors
- Duplicate product entries in CSV output
- Empty title handling in DataFrame
- Syntax errors in extraction functions
- Review extraction format inconsistency

### Security
- Implemented User-Agent rotation to avoid detection
- Added try-except blocks for graceful error handling
- Added delays between requests to prevent rate limiting

---

## Version History

| Version | Date | Description |
|---------|------|-------------|
| **1.0.0** | 2026-07-21 | Initial production release with requests + BeautifulSoup |
| 0.1.0 | 2026-07-15 | Development version (internal testing) |

---

## How to Update Changelog

When making changes to the project:

1. **Added** - New features or functionality
2. **Changed** - Changes to existing functionality
3. **Deprecated** - Features that will be removed in future
4. **Removed** - Features that have been removed
5. **Fixed** - Bug fixes
6. **Security** - Security improvements

### Example Entry

```markdown
## [1.1.0] - 2026-08-01

### Added
- Multi-page scraping support
- Price history tracking feature

### Fixed
- Fixed selector for product price (Amazon HTML structure change)
- Fixed empty title handling

### Changed
- Updated User-Agent headers for better compatibility
```

---

*Last Updated: 2026-07-21*