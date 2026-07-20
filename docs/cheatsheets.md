# Amazon Web Scraping - Cheat Sheet

---

## Quick Commands

### Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate venv (Windows)
venv\Scripts\activate

# Activate venv (Mac/Linux)
source venv/bin/activate

# Deactivate venv
deactivate

# Delete venv (Windows)
rmdir /s venv

# Delete venv (Mac/Linux)
rm -rf venv
```

---

## Jupyter Notebook Commands

```bash
# Install Jupyter
pip install jupyter

# Launch Jupyter Notebook
jupyter notebook

# Launch Jupyter Lab
jupyter lab

# Open specific notebook
jupyter notebook amazon_scrape_final.ipynb

# Convert notebook to Python script
jupyter nbconvert --to script amazon_scrape_final.ipynb

# List running notebooks
jupyter notebook list

# Stop Jupyter
Ctrl + C

# Restart kernel and run all cells
Kernel → Restart & Run All
```

---

## Python Package Management

### Install Dependencies

```bash
# Install all requirements
pip install -r requirements.txt

# Install specific packages
pip install requests==2.31.0
pip install beautifulsoup4==4.12.0
pip install lxml==4.9.0
pip install pandas==2.0.0
pip install numpy==1.24.0
pip install jupyter==1.0.0

# Upgrade pip
python -m pip install --upgrade pip

# List installed packages
pip list

# Freeze requirements
pip freeze > requirements.txt
```

### requirements.txt

```txt
requests==2.31.0
beautifulsoup4==4.12.0
lxml==4.9.0
pandas==2.0.0
numpy==1.24.0
jupyter==1.0.0
```

### Verify Installation

```bash
# Check Python version
python --version

# Test imports
python -c "import requests; print('Requests OK')"
python -c "from bs4 import BeautifulSoup; print('BeautifulSoup OK')"
python -c "import pandas as pd; print('Pandas OK')"
python -c "import numpy as np; print('NumPy OK')"
```

---

## Code Snippets

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

### HTTP Headers

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

### Helper Functions

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
```

### Extraction Functions

```python
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

### Main Scraping Script

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

# Run multi-product scraper
df = scrape_multiple_products(POPULAR_PRODUCTS[:3], max_products=3)
df.to_csv('amazon_all_products.csv', index=False)
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

---

## BeautifulSoup Selectors Reference

### Amazon Product Page Selectors

| Data Point | Selector | Code |
|------------|----------|------|
| Title | `span#productTitle` | `soup.find("span", attrs={"id": 'productTitle'})` |
| Price (Primary) | `.a-price .a-offscreen` | `soup.select_one(".a-price .a-offscreen")` |
| Price (Legacy) | `span#priceblock_ourprice` | `soup.find("span", attrs={'id': 'priceblock_ourprice'})` |
| Price (Deal) | `span#priceblock_dealprice` | `soup.find("span", attrs={'id': 'priceblock_dealprice'})` |
| Price (Alt) | `span.a-price a-text-price` | `soup.find("span", class_="a-price a-text-price")` |
| Rating | `span.a-icon-alt` | `soup.find("span", attrs={'class': 'a-icon-alt'})` |
| Rating (Alt) | `i.a-icon-star` | `soup.find("i", class_="a-icon-star")` |
| Review Count | `span#acrCustomerReviewText` | `soup.find("span", attrs={'id': 'acrCustomerReviewText'})` |
| Review Count (Alt) | `#acrCustomerReviewText` | `soup.select_one("#acrCustomerReviewText")` |
| Availability | `div#availability` | `soup.find("div", attrs={'id': 'availability'})` |
| Availability (Alt) | `#availability span` | `soup.select_one("#availability span")` |

### Search Result Selectors

| Data Point | Selector | Code |
|------------|----------|------|
| Product Links | `a.a-link-normal.s-no-outline` | `soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})` |
| Product Title (Search) | `span.a-size-medium` | `product.find('span', {'class': 'a-size-medium'})` |

---

## Pandas Commands Reference

### Read and Write CSV

```python
# Read CSV
df = pd.read_csv('amazon_data.csv')

# Read with specific encoding
df = pd.read_csv('amazon_data.csv', encoding='utf-8')

# Write CSV
df.to_csv('amazon_data.csv', header=True, index=False)

# Write without header
df.to_csv('amazon_data.csv', header=False, index=False)
```

### Inspect DataFrame

```python
# View first 5 rows
df.head()

# View last 5 rows
df.tail()

# Get shape (rows, columns)
df.shape

# Get column names
df.columns

# Get info (data types, nulls)
df.info()

# Get descriptive stats
df.describe()

# Get value counts
df['column'].value_counts()

# Check for duplicates
df.duplicated().sum()
```

### Clean Data

```python
# Replace empty strings with NaN
df['column'].replace('', np.nan, inplace=True)

# Drop rows with NaN in specific column
df = df.dropna(subset=['column'])

# Drop duplicates
df = df.drop_duplicates()

# Drop duplicates by specific column
df = df.drop_duplicates(subset=['column'], keep='first')

# Strip whitespace
df['column'] = df['column'].str.strip()

# Fill missing values
df['column'] = df['column'].fillna('Unknown')

# Convert data types
df['column'] = df['column'].astype(str)
df['numeric'] = df['numeric'].astype(float)

# Reset index
df = df.reset_index(drop=True)
df.index = range(1, len(df) + 1)
```

### Filter Data

```python
# Filter by value
filtered_df = df[df['column'] == 'value']

# Filter by multiple conditions
filtered_df = df[(df['column1'] == 'value1') & (df['column2'] == 'value2')]

# Filter by string contains
filtered_df = df[df['column'].str.contains('keyword')]

# Filter by not null
filtered_df = df[df['column'].notna()]

# Filter by string contains (case insensitive)
mask = df['column'].str.contains('keyword', case=False, na=False)
filtered_df = df[mask]
```

### Group and Aggregate

```python
# Group by column and count
df.groupby('column').size()

# Group by column and sum
df.groupby('column')['numeric'].sum()

# Group by column and mean
df.groupby('column')['numeric'].mean()

# Group by multiple columns
df.groupby(['col1', 'col2']).size()
```

---

## Requests Commands Reference

### Basic Requests

```python
import requests

# GET request
response = requests.get(url)

# GET with headers
response = requests.get(url, headers=headers)

# GET with timeout
response = requests.get(url, timeout=10)

# GET with params
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get(url, params=params)

# Check status
if response.status_code == 200:
    print("Success")
else:
    print(f"Failed: {response.status_code}")
```

### Response Handling

```python
# Get HTML content
html = response.text

# Get raw content
content = response.content

# Get JSON
data = response.json()

# Get headers
headers = response.headers

# Get cookies
cookies = response.cookies
```

---

## Error Handling Patterns

### Try-Except for Extraction

```python
def extract_data(soup):
    try:
        data = soup.find('selector')
        return data.text.strip()
    except AttributeError:
        return ""  # Return empty string on failure

def extract_data_with_fallback(soup):
    try:
        data = soup.find('selector1')
        if data:
            return data.text.strip()
    except:
        pass

    try:
        data = soup.find('selector2')
        if data:
            return data.text.strip()
    except:
        pass

    return ""
```

### Try-Except for HTTP Requests

```python
import time

def fetch_page(url, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(2 ** attempt)  # Exponential backoff
    return None
```

---

## Git Commands

```bash
# Initialize repository
git init

# Check status
git status

# Add files
git add .
git add filename.py

# Commit
git commit -m "Initial commit"

# View history
git log --oneline

# Create branch
git branch feature-name

# Switch branch
git checkout feature-name

# Merge branch
git merge feature-name

# Push to remote
git push origin main

# Pull from remote
git pull origin main

# View remote
git remote -v
```

---

## Common Amazon Selector Issues

### If Selector Not Working

```python
# Debug: Print HTML snippet
print(soup.prettify()[:1000])

# Debug: Print specific element HTML
element = soup.find('span', id='productTitle')
print(element.prettify() if element else "Not found")

# Try alternative selectors
title_alt1 = soup.find('h1', id='title')
title_alt2 = soup.select('#productTitle')
price_alt = soup.select('.a-price .a-offscreen')
rating_alt = soup.select('.a-icon-alt')
reviews_alt = soup.select('#acrCustomerReviewText')
```

### Common Structure Changes

| Old Selector | New Alternative |
|--------------|-----------------|
| `span#priceblock_ourprice` | `.a-price .a-offscreen` |
| `span#priceblock_dealprice` | `.a-price .a-offscreen` |
| `i.a-icon-star` | `span.a-icon-alt` |
| `span#acrCustomerReviewText` | `[data-hook="total-review-count"]` |

---

## Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| 403 Forbidden | Update User-Agent headers |
| No data extracted | Check selectors are still valid |
| Empty CSV | Verify links_list has data |
| AttributeError | Add try-except blocks |
| ModuleNotFoundError | Install missing packages |
| Price N/A | Product may be discontinued or geo-blocked |
| Empty title | Product may not have title element |
| Connection timeout | Increase timeout value |
| Duplicate products | Use `drop_duplicates()` |

---

## URLs

| Resource | URL |
|----------|-----|
| Amazon Search | `https://www.amazon.com/s?k=KEYWORD` |
| Repository | `https://github.com/ArkanTsabit123/Amazon-Web-Scrapping` |
| BeautifulSoup Docs | `https://www.crummy.com/software/BeautifulSoup/` |
| Requests Docs | `https://docs.python-requests.org/` |
| Pandas Docs | `https://pandas.pydata.org/docs/` |

---

## Quick Commands Reference Card

```bash
# START
jupyter notebook

# RUN SCRAPER (Python script)
python amazon_scrape_final.py

# RUN SCRAPER (Jupyter)
jupyter notebook amazon_scrape_final.ipynb

# INSTALL DEPENDENCIES
pip install -r requirements.txt

# ACTIVATE VENV
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# GIT COMMANDS
git add .
git commit -m "message"
git push origin main

# JUPYTER SHORTCUTS
# Run cell: Shift + Enter
# Run all cells: Kernel → Restart & Run All
# Save: Ctrl + S
```

---

*Last Updated: 2026-07-21*