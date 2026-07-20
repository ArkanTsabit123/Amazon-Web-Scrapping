# Changelog - Amazon Web Scraping Project

---

## [1.0.0] - 2026-07-20

### Added
- Initial project setup and repository creation
- `amazon_scrape_final.ipynb` - Final working scraper implementation
- `amazon_web_scraping_tutorial.ipynb` - Step-by-step tutorial notebook
- Working scraper with PS5 product data extraction
- 5 extraction functions:
  - `get_title()` - Extract product title from `#productTitle`
  - `get_price()` - Extract product price from `#priceblock_ourprice` or `#priceblock_dealprice`
  - `get_rating()` - Extract product rating from `.a-icon-star` or `.a-icon-alt`
  - `get_review_count()` - Extract review count from `#acrCustomerReviewText`
  - `get_availability()` - Extract availability from `#availability`
- HTTP request configuration with custom User-Agent headers
- Search result scraping from Amazon
- Data cleaning pipeline using Pandas
- CSV export functionality (`amazon_data.csv`)
- Project documentation:
  - `README.md` - Project overview and quick start guide
  - `docs/blueprint.md` - Technical blueprint
  - `docs/cheatsheets.md` - Quick reference commands
  - `docs/verification_checklist.md` - Testing checklist
  - `CHANGELOG.md` - This file
- Screenshots documentation (8 images):
  - `images/folder_structure.png` - Project folder structure
  - `images/scraping_result_Jupyter.png` - Scraping results in Jupyter
  - `images/csv_output_excel.png` - CSV output in Excel
  - `images/Function to extract Product Title.png`
  - `images/Function to extract Product Price.png`
  - `images/Function to extract Product Rating.png`
  - `images/Function to extract Number of User Reviews.png`
  - `images/Function to extract Availability Status.png`
- `.gitignore` for Python and Jupyter Notebook files

### Changed
- Improved final scraper code structure
- Simplified README with clear project structure and concise description

### Security
- Implemented User-Agent headers to avoid detection
- Added try-except blocks for graceful error handling

---

## [Unreleased]

### Planned Features
- Multi-page scraping support
- Price history tracking
- Product reviews extraction
- Database integration
- Scheduled scraping
- Email alerts for price drops
- API deployment with FastAPI
- Data visualization dashboard

---

*Last Updated: 2026-07-20*