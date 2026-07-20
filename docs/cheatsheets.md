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
```

### HTTP Headers

```python
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}
```

### Extraction Functions

```python
def get_title(soup):
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        return title.text.strip()
    except AttributeError:
        return ""

def get_price(soup):
    try:
        return soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip()
    except AttributeError:
        try:
            return soup.find("span", attrs={'id': 'priceblock_dealprice'}).string.strip()
        except:
            return ""

def get_rating(soup):
    try:
        return soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            return soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            return ""

def get_review_count(soup):
    try:
        return soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        return ""

def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        return available.find("span").string.strip()
    except AttributeError:
        return "Not Available"
```

### Main Scraping Script

```python
if __name__ == '__main__':
    URL = "https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})
    links_list = [link.get('href') for link in links]
    
    d = {"title": [], "price": [], "rating": [], "reviews": [], "availability": []}
    
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_review_count(new_soup))
        d['availability'].append(get_availability(new_soup))
    
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)
```

---

## BeautifulSoup Selectors Reference

### Amazon Product Page Selectors

| Data Point | Selector | Code |
|------------|----------|------|
| Title | `span#productTitle` | `soup.find("span", attrs={"id": 'productTitle'})` |
| Price (Regular) | `span#priceblock_ourprice` | `soup.find("span", attrs={'id': 'priceblock_ourprice'})` |
| Price (Deal) | `span#priceblock_dealprice` | `soup.find("span", attrs={'id': 'priceblock_dealprice'})` |
| Rating | `i.a-icon-star` | `soup.find("i", attrs={'class': 'a-icon a-icon-star'})` |
| Rating (Alt) | `span.a-icon-alt` | `soup.find("span", attrs={'class': 'a-icon-alt'})` |
| Review Count | `span#acrCustomerReviewText` | `soup.find("span", attrs={'id': 'acrCustomerReviewText'})` |
| Availability | `div#availability` | `soup.find("div", attrs={'id': 'availability'})` |

### Search Result Selectors

| Data Point | Selector | Code |
|------------|----------|------|
| Product Links | `a.a-link-normal.s-no-outline` | `soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})` |

---

## Pandas Commands Reference

### Read and Write CSV

```python
# Read CSV
df = pd.read_csv('amazon_data.csv')

# Write CSV
df.to_csv('amazon_data.csv', header=True, index=False)

# Read with specific encoding
df = pd.read_csv('amazon_data.csv', encoding='utf-8')
```

### Inspect DataFrame

```python
# View first 5 rows
df.head()

# View last 5 rows
df.tail()

# Get shape
df.shape

# Get column names
df.columns

# Get info
df.info()

# Get descriptive stats
df.describe()
```

### Clean Data

```python
# Replace empty strings with NaN
df['column'].replace('', np.nan, inplace=True)

# Drop rows with NaN in specific column
df = df.dropna(subset=['column'])

# Drop duplicates
df = df.drop_duplicates()

# Strip whitespace
df['column'] = df['column'].str.strip()

# Fill missing values
df['column'] = df['column'].fillna('Unknown')

# Convert data types
df['column'] = df['column'].astype(str)
df['numeric'] = df['numeric'].astype(float)
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
```

---

## Common Amazon Selector Issues

### If Selector Not Working

```python
# Debug: Print HTML snippet
print(soup.prettify()[:1000])

# Try alternative selectors
title_alt1 = soup.find('h1', id='title')
title_alt2 = soup.select('#productTitle')
price_alt = soup.select('.a-price .a-offscreen')
```

### Common Structure Changes

| Old Selector | New Alternative |
|--------------|-----------------|
| `span#priceblock_ourprice` | `.a-price .a-offscreen` |
| `span#priceblock_dealprice` | `.a-price .a-offscreen` |
| `i.a-icon-star` | `span.a-icon-alt` |

---

## Quick Troubleshooting

| Issue | Solution |
|-------|----------|
| 403 Forbidden | Update User-Agent headers |
| No data extracted | Check selectors are still valid |
| Connection timeout | Increase timeout value |
| Empty CSV | Verify links_list has data |
| AttributeError | Add try-except blocks |
| ModuleNotFoundError | Install missing packages |

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

*Last Updated: 2026-07-20*