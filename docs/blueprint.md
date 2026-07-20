# AMAZON WEB SCRAPING - TECHNICAL BLUEPRINT

## Document Information

| Property | Value |
|----------|-------|
| **Version** | 1.0.0 |
| **Last Updated** | 2026-07-21 |
| **Status** | Production Ready |
| **Development Environment** | Jupyter Notebook / Python Script |
| **Output Format** | CSV (Pandas DataFrame) |
| **Target** | Amazon Search Result Pages |

---

## Project Overview

### Core Goals

1. Build web scraping pipeline to extract product data from Amazon search results
2. Scrape product details from each product link found in search results
3. Extract 5 key data points: Title, Price, Rating, Review Count, Availability
4. Clean and structure scraped data using Pandas
5. Save results in CSV format for further analysis
6. Support multi-product scraping with popular keywords

### Success Metrics

- Successfully scrape product links from search result page
- Extract 5 data points per product
- Handle missing data gracefully
- Generate clean CSV output ready for analysis
- Support multi-product scraping

---

## System Architecture

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    AMAZON WEB SCRAPING PIPELINE                             │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  STEP 1: SEARCH REQUEST                                            │    │
│  │  - requests.get() to Amazon search URL                             │    │
│  │  - URL: https://www.amazon.com/s?k=playstation+5                   │    │
│  │  - Custom User-Agent headers                                       │    │
│  └──────────────────────────┬──────────────────────────────────────────┘    │
│                             │                                               │
│                             ▼                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  STEP 2: EXTRACT PRODUCT LINKS                                     │    │
│  │  - Parse search results HTML using BeautifulSoup                   │    │
│  │  - Find all links with class 'a-link-normal s-no-outline'          │    │
│  │  - Build list of product detail page URLs                          │    │
│  └──────────────────────────┬──────────────────────────────────────────┘    │
│                             │                                               │
│                             ▼                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  STEP 3: SCRAPE EACH PRODUCT                                       │    │
│  │  ┌───────────────────────────────────────────────────────────┐     │    │
│  │  │  For each product link:                                   │     │    │
│  │  │  - requests.get() to product detail page                 │     │    │
│  │  │  - Parse HTML with BeautifulSoup                         │     │    │
│  │  │  - Extract: Title, Price, Rating, Reviews, Availability  │     │    │
│  │  └───────────────────────────────────────────────────────────┘     │    │
│  └──────────────────────────┬──────────────────────────────────────────┘    │
│                             │                                               │
│                             ▼                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  STEP 4: DATA CLEANING & EXPORT                                    │    │
│  │  - Build Pandas DataFrame                                          │    │
│  │  - Remove rows with missing titles                                 │    │
│  │  - Export to CSV: amazon_data.csv                                  │    │
│  └─────────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Details

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                          DATA FLOW PIPELINE                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Step 1: SEARCH REQUEST                                                    │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Input:  Search keyword (e.g., "playstation 5")                    │   │
│  │  URL:    https://www.amazon.com/s?k=playstation+5                  │   │
│  │  Action: requests.get(URL, headers=HEADERS)                        │   │
│  │  Output: HTML Response (search results page)                       │   │
│  │  Time:   2-5 seconds                                               │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  Step 2: EXTRACT PRODUCT LINKS                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Input:  Search results HTML                                       │   │
│  │  Action: soup.find_all('a', class_='a-link-normal s-no-outline')   │   │
│  │  Output: List of product detail page URLs                          │   │
│  │  Time:   < 1 second                                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  Step 3: SCRAPE EACH PRODUCT                                              │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Input:  List of product URLs                                      │   │
│  │  Actions:                                                          │   │
│  │   1. For each URL: requests.get() to product page                  │   │
│  │   2. BeautifulSoup parsing                                        │   │
│  │   3. Extract:                                                      │   │
│  │      - Title: span#productTitle                                   │   │
│  │      - Price: span#priceblock_ourprice or #priceblock_dealprice   │   │
│  │      - Rating: i.a-icon-star or span.a-icon-alt                   │   │
│  │      - Reviews: span#acrCustomerReviewText                        │   │
│  │      - Availability: div#availability span                        │   │
│  │  Output: Dictionary with product data                             │   │
│  │  Time:   2-5 seconds per product                                  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                    │                                        │
│                                    ▼                                        │
│  Step 4: DATA CLEANING & EXPORT                                            │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │  Input:  List of product dictionaries                              │   │
│  │  Actions:                                                          │   │
│  │   1. pd.DataFrame.from_dict(d)                                    │   │
│  │   2. Replace empty titles with NaN                                 │   │
│  │   3. Drop rows with missing titles                                 │   │
│  │   4. df.to_csv('amazon_data.csv')                                  │   │
│  │  Output: CSV file with product data                               │   │
│  │  Time:   < 1 second                                                │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

| Layer | Technology | Version | Purpose |
|-------|-----------|---------|---------|
| Programming | Python | 3.10+ | Primary language |
| HTTP Client | Requests | 2.31.0 | Send HTTP requests |
| HTML Parser | BeautifulSoup4 | 4.12.0 | Parse HTML content |
| Parser Engine | lxml | 4.9.0 | Fast HTML parsing |
| Data Processing | Pandas | 2.0.0 | Data manipulation |
| Numerical | NumPy | 1.24.0 | Handle missing values |
| Development | Jupyter Notebook | Latest | Interactive development |

---

## Data Model Design

### Output Schema: `amazon_data.csv`

| Column | Type | Description | HTML Source |
|--------|------|-------------|-------------|
| `title` | STRING | Product name | `span#productTitle` |
| `price` | STRING | Current price (with $) | `span#priceblock_ourprice` or `span#priceblock_dealprice` |
| `rating` | STRING | Product rating (e.g., "4.8 out of 5 stars") | `i.a-icon-star` or `span.a-icon-alt` |
| `reviews` | STRING | Number of reviews (e.g., "8 ratings") | `span#acrCustomerReviewText` |
| `availability` | STRING | Stock status | `div#availability span` |

### Example Data Record

| Field | Example Value |
|-------|--------------|
| title | "PlayStation 5 Console (PS5)" |
| price | "$499.99" |
| rating | "4.8 out of 5 stars" |
| reviews | "(9,215)" |
| availability | "Only 1 left in stock - order soon." |

---

## Project Structure

```
Amazon-Web-Scrapping/
│
├── README.md
├── .gitignore
├── requirements.txt
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
│
├── amazon_scrape_final.ipynb
├── amazon_web_scraping_tutorial.ipynb
├── amazon_data.csv
├── amazon_all_products.csv
├── amazon_scrape_final.py
│
├── docs/
│   ├── blueprint.md
│   ├── cheatsheets.md
│   └── verification_checklist.md
│
└── images/
    ├── folder_structure.png
    ├── csv_output_excel.png
    ├── scraping_result_Jupyter.png
    ├── architecture-diagram.png
    ├── Function to extract Product Title.png
    ├── Function to extract Product Price.png
    ├── Function to extract Product Rating.png
    ├── Function to extract Number of User Reviews.png
    └── Function to extract Availability Status.png
```

---

## Screenshots Documentation

### Image Inventory

| No | Filename | Status | Description |
|----|----------|--------|-------------|
| 1 | `folder_structure.png` | Available | Project folder structure in VS Code |
| 2 | `csv_output_excel.png` | Available | Exported CSV file opened in Excel |
| 3 | `scraping_result_Jupyter.png` | Available | Scraping results displayed in Jupyter Notebook |
| 4 | `architecture-diagram.png` | Available | System architecture diagram |
| 5 | `Function to extract Product Title.png` | Available | Title extraction function |
| 6 | `Function to extract Product Price.png` | Available | Price extraction function |
| 7 | `Function to extract Product Rating.png` | Available | Rating extraction function |
| 8 | `Function to extract Number of User Reviews.png` | Available | Review count extraction function |
| 9 | `Function to extract Availability Status.png` | Available | Availability extraction function |

### Screenshot Summary

| Category | Count | Files |
|----------|-------|-------|
| Project Structure | 1 | `folder_structure.png` |
| Architecture | 1 | `architecture-diagram.png` |
| Extraction Functions | 5 | Title, Price, Rating, Reviews, Availability |
| Results | 2 | Jupyter output, CSV output |
| **Total** | **9** | All available in `images/` directory |

---

## Implementation Details

### Import Libraries

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import time
import random
from typing import Dict, List, Optional, Tuple
```

### HTTP Request Configuration

```python
USER_AGENTS: List[str] = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/113.0.0.0 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/112.0.0.0 Safari/537.36',
]

BASE_HEADERS: Dict[str, str] = {
    'Accept-Language': 'en-US, en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
}

def get_request_headers() -> Dict[str, str]:
    headers = BASE_HEADERS.copy()
    headers['User-Agent'] = random.choice(USER_AGENTS)
    return headers
```

### Selectors Configuration

```python
TITLE_SELECTORS: List[Tuple[str, Dict[str, str]]] = [
    ('span', {'id': 'productTitle'}),
    ('h1', {'id': 'title'}),
]

PRICE_SELECTORS: List = [
    '.a-price .a-offscreen',
    ('span', {'id': 'priceblock_ourprice'}),
    ('span', {'id': 'priceblock_dealprice'}),
    ('span', {'class': 'a-price a-text-price'}),
]

RATING_SELECTORS: List = [
    ('span', {'class': 'a-icon-alt'}),
    ('i', {'class': 'a-icon a-icon-star a-star-4-5'}),
    ('i', {'class': 'a-icon-star'}),
    '.a-icon-alt',
]

REVIEW_SELECTORS: List = [
    ('span', {'id': 'acrCustomerReviewText'}),
    '#acrCustomerReviewText',
]

AVAILABILITY_SELECTORS: List = [
    ('div', {'id': 'availability'}),
    '#availability span',
]
```

### Extraction Functions

```python
def find_element(soup: BeautifulSoup, selectors: List) -> Optional[BeautifulSoup]:
    for selector in selectors:
        try:
            if isinstance(selector, tuple):
                tag, attrs = selector
                element = soup.find(tag, attrs=attrs)
            else:
                element = soup.select_one(selector)
            if element:
                return element
        except (AttributeError, TypeError):
            continue
    return None

def get_text(element, default: str = "") -> str:
    if element:
        text = element.get_text().strip()
        return text if text else default
    return default

def extract_title(soup: BeautifulSoup) -> str:
    element = find_element(soup, TITLE_SELECTORS)
    return get_text(element)

def extract_price(soup: BeautifulSoup) -> str:
    try:
        price = soup.select_one(".a-price .a-offscreen")
        if price:
            text = price.get_text().strip()
            if text and '$' in text:
                return text
    except:
        pass

    try:
        price = soup.find("span", attrs={'id': 'priceblock_ourprice'})
        if price:
            text = price.string.strip()
            if text and '$' in text:
                return text
    except:
        pass

    try:
        price = soup.find("span", attrs={'id': 'priceblock_dealprice'})
        if price:
            text = price.string.strip()
            if text and '$' in text:
                return text
    except:
        pass

    try:
        price = soup.find("span", class_="a-price a-text-price")
        if price:
            text = price.get_text().strip()
            if text and '$' in text:
                return text
    except:
        pass

    return ""

def extract_rating(soup: BeautifulSoup) -> str:
    try:
        rating = soup.find("span", attrs={'class': 'a-icon-alt'})
        if rating:
            text = rating.get_text().strip()
            if text and 'out of 5 stars' in text:
                return text
    except:
        pass

    try:
        rating = soup.find("i", class_="a-icon-star")
        if rating:
            parent = rating.find_parent()
            if parent:
                text = parent.get_text().strip()
                if text and 'out of 5 stars' in text:
                    return text
    except:
        pass

    return ""

def extract_review_count(soup: BeautifulSoup) -> str:
    try:
        reviews = soup.find("span", attrs={'id': 'acrCustomerReviewText'})
        if reviews:
            text = reviews.get_text().strip()
            if text:
                return text
    except:
        pass

    try:
        reviews = soup.select_one("#acrCustomerReviewText")
        if reviews:
            text = reviews.get_text().strip()
            if text:
                return text
    except:
        pass

    return ""

def extract_availability(soup: BeautifulSoup) -> str:
    element = find_element(soup, AVAILABILITY_SELECTORS)
    if element:
        if element.name == 'div':
            span = element.find('span')
            if span:
                text = span.get_text().strip()
                if text:
                    return text
        text = element.get_text().strip()
        if text:
            return text
    return "Not Available"
```

### Product Scraper Functions

```python
def extract_product_links(soup: BeautifulSoup) -> List[str]:
    links = soup.find_all('a', attrs={'class': 'a-link-normal s-no-outline'})
    result = []

    for link in links:
        href = link.get('href')
        if href and '/dp/' in href:
            parent = link.find_parent()
            if parent and 'Renewed' in parent.text:
                continue
            result.append(href)

    return list(dict.fromkeys(result))

def fetch_page(url: str, headers: Dict[str, str]) -> Optional[BeautifulSoup]:
    try:
        response = requests.get(url, headers=headers, timeout=15)
        response.raise_for_status()
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException:
        return None

def scrape_product_page(product_url: str, headers: Dict[str, str]) -> Optional[Dict[str, str]]:
    time.sleep(random.uniform(2, 4))
    soup = fetch_page(product_url, headers)
    if not soup:
        return None
    return {
        'title': extract_title(soup),
        'price': extract_price(soup),
        'rating': extract_rating(soup),
        'reviews': extract_review_count(soup),
        'availability': extract_availability(soup),
    }
```

### Main Scraping Engine

```python
def scrape_amazon_products(
    search_keyword: str = "playstation 5",
    max_products: int = 10
) -> pd.DataFrame:
    print(f"Searching for: {search_keyword}")
    print(f"Max products: {max_products}\n")

    encoded_keyword = search_keyword.replace(' ', '+')
    search_url = f"https://www.amazon.com/s?k={encoded_keyword}&ref=nb_sb_noss_2"
    print(f"URL: {search_url}\n")

    headers = get_request_headers()
    soup = fetch_page(search_url, headers)

    if not soup:
        print("Search request failed")
        return pd.DataFrame()

    product_links = extract_product_links(soup)
    product_links = [link for link in product_links if 'renewed' not in link.lower()]
    product_links = product_links[:max_products]

    print(f"Found {len(product_links)} product links")

    if not product_links:
        print("No product links found")
        return pd.DataFrame()

    data = {
        'title': [],
        'price': [],
        'rating': [],
        'reviews': [],
        'availability': []
    }

    print(f"\nScraping {len(product_links)} products...\n")

    for index, link in enumerate(product_links, 1):
        if link.startswith('/'):
            product_url = f"https://www.amazon.com{link}"
        else:
            product_url = f"https://www.amazon.com/{link}"

        print(f"  {index}. Scraping: {product_url[:50]}...")

        headers = get_request_headers()
        product_data = scrape_product_page(product_url, headers)

        if product_data:
            data['title'].append(product_data['title'])
            data['price'].append(product_data['price'])
            data['rating'].append(product_data['rating'])
            data['reviews'].append(product_data['reviews'])
            data['availability'].append(product_data['availability'])

            title = product_data['title'][:50]
            if len(product_data['title']) > 50:
                title += '...'

            price = product_data['price'] if product_data['price'] else 'N/A'
            rating = product_data['rating'] if product_data['rating'] else 'N/A'

            print(f"     Price: {price} | Rating: {rating}")
        else:
            print(f"     Failed to scrape product")

    df = pd.DataFrame(data)

    df['title'] = df['title'].replace('', np.nan)
    df = df.dropna(subset=['title'])
    df = df.reset_index(drop=True)
    df.index = range(1, len(df) + 1)

    print(f"\nScraping complete! Saved {len(df)} products")
    return df
```

### Multi-Product Scraping

```python
POPULAR_PRODUCTS: List[str] = [
    "airpods pro 2",
    "echo dot 5th gen",
    "iphone 15 pro max",
    "sony wh-1000xm5",
    "kindle paperwhite",
    "samsung s24 ultra",
    "apple watch series 9",
    "playstation 5 console",
    "ipad 10th generation",
    "nespresso vertuoplus"
]

def combine_scraped_data(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    if not dataframes:
        print("No data available")
        return pd.DataFrame()

    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df.index = range(1, len(combined_df) + 1)

    print(f"\n{'='*60}")
    print(f"Total products scraped: {len(combined_df)}")
    print(f"{'='*60}")

    return combined_df

def scrape_multiple_products(
    keywords: List[str],
    max_products: int = 5
) -> pd.DataFrame:
    all_data = []

    for keyword in keywords:
        print(f"\n{'='*60}")
        print(f"Scraping: {keyword}")
        print(f"{'='*60}\n")

        product_df = scrape_amazon_products(
            search_keyword=keyword,
            max_products=max_products
        )

        if not product_df.empty:
            product_df['keyword'] = keyword
            all_data.append(product_df)
            print(f"Success: {keyword} - {len(product_df)} products found")
        else:
            print(f"Failed: {keyword} - No products found")

        time.sleep(5)

    return combine_scraped_data(all_data)
```

### Export Functions

```python
def export_to_csv(dataframe: pd.DataFrame, filename: str = 'amazon_data.csv') -> None:
    if dataframe.empty:
        print("No data to export")
        return

    dataframe.to_csv(filename, index=False)
    print(f"Exported to {filename}")

def print_summary(dataframe: pd.DataFrame) -> None:
    if dataframe.empty:
        print("No data to summarize")
        return

    print("\nSummary:")
    print(f"  Total products: {len(dataframe)}")
    print(f"  Products with price: {dataframe['price'].notna().sum()}")
    print(f"  Products with rating: {dataframe['rating'].notna().sum()}")
    print(f"  Products with reviews: {dataframe['reviews'].notna().sum()}")
    print(f"  Products with availability: {dataframe['availability'].notna().sum()}")

    price_values = dataframe['price'].dropna()
    if not price_values.empty:
        numeric_prices = []

        for price in price_values:
            try:
                numeric = float(price.replace('$', '').replace(',', '').strip())
                numeric_prices.append(numeric)
            except (ValueError, AttributeError):
                continue

        if numeric_prices:
            print(f"\n  Price Range: ${min(numeric_prices):.2f} - ${max(numeric_prices):.2f}")
            print(f"  Average Price: ${sum(numeric_prices) / len(numeric_prices):.2f}")
```

### Main Entry Point

```python
if __name__ == "__main__":
    print("\n" + "="*60)
    print("AMAZON WEB SCRAPING - FINAL SCRAPER")
    print("="*60 + "\n")

    scraped_data = scrape_multiple_products(
        keywords=POPULAR_PRODUCTS[:3],
        max_products=3
    )

    if not scraped_data.empty:
        print("\nScraped Data:")
        print(scraped_data.to_string())
        export_to_csv(scraped_data, 'amazon_all_products.csv')
        print_summary(scraped_data)
    else:
        print("No data was successfully scraped")
```

### Sample Output

```
                                               title   price               rating          reviews              availability
0   OUBANG 2 Pack Controllers Work with PS4 Contro...  $37.99  4.8 out of 5 stars        8 ratings           Not Available
1                     PlayStation 4 Slim 1TB Console                  4.7 out of 5 stars   15,164 ratings                      
2   PlayStation 4 Slim 1TB Console - Only On PlayS...                  4.8 out of 5 stars    8,860 ratings   Only 3 left in stock - order soon
3                  Hunting Simulator - PlayStation 4  $16.61  4.3 out of 5 stars      937 ratings           Not Available
4   BlueFire Professional 3.5mm PS4 Gaming Headset...                  4.4 out of 5 stars    8,257 ratings           Not Available
```

---

## Anti-Scraping Measures

| Challenge | Solution |
|-----------|----------|
| IP Blocking | Use custom User-Agent headers |
| Rate Limiting | Add delays between requests (2-4 seconds) |
| Amazon Detection | Rotate User-Agent headers |

---

## Performance Specifications

| Metric | Value |
|--------|-------|
| Products per run | 10-50 (varies by keyword) |
| Data points per product | 5 fields |
| Scraping speed | 2-5 seconds per product |
| Memory usage | 50-100 MB |

---

## Troubleshooting Guide

| Issue | Solution |
|-------|----------|
| 403 Forbidden | Update User-Agent headers |
| Empty title | Product may not have title element |
| Price not found | Product may use different price selector |
| Rating not found | Product may not have reviews |
| Empty links_list | Search result structure may have changed |
| Price N/A | Product may be discontinued or geo-blocked |

---

## Legal and Ethical Considerations

This project is for educational purposes only. Users must:
- Respect Amazon's Terms of Service
- Implement reasonable rate limits
- Use official Amazon Product Advertising API for commercial applications

---

## References

| Resource | URL |
|----------|-----|
| Repository | https://github.com/ArkanTsabit123/Amazon-Web-Scrapping |
| BeautifulSoup Docs | https://www.crummy.com/software/BeautifulSoup/ |
| Requests Docs | https://docs.python-requests.org/ |
| Pandas Docs | https://pandas.pydata.org/docs/ |

---

*Last Updated: 2026-07-21*