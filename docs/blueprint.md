# AMAZON WEB SCRAPING - TECHNICAL BLUEPRINT

## Document Information

| Property | Value |
|----------|-------|
| **Version** | 1.0.0 |
| **Last Updated** | 2026-07-20 |
| **Status** | Development Ready |
| **Development Environment** | Jupyter Notebook |
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

### Success Metrics

- Successfully scrape all product links from search result page
- Extract 5 data points per product
- Handle missing data gracefully
- Generate clean CSV output ready for analysis

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
│  │  - URL: https://www.amazon.com/s?k=playstation+4                   │    │
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
│  │  Input:  Search keyword (e.g., "playstation 4")                    │   │
│  │  URL:    https://www.amazon.com/s?k=playstation+4                  │   │
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
| Programming | Python | 3.9+ | Primary language |
| HTTP Client | Requests | Latest | Send HTTP requests |
| HTML Parser | BeautifulSoup4 | Latest | Parse HTML content |
| Data Processing | Pandas | Latest | Data manipulation |
| Numerical | NumPy | Latest | Handle missing values |
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

### Example Data Record (from actual output)

| Field | Example Value |
|-------|--------------|
| title | "OUBANG 2 Pack Controllers Work with PS4 Contro..." |
| price | "$37.99" |
| rating | "4.8 out of 5 stars" |
| reviews | "8 ratings" |
| availability | "Not Available" |

---

## Project Structure

```
Amazon-Web-Scrapping/
│
├── README.md
├── .gitignore
│
├── amazon_web_scraping_tutorial.ipynb
├── amazon_scrape_final.ipynb
├── amazon_data.csv
│
├── docs/
│   ├── blueprint.md
│   ├── cheatsheets.md
│   └── verification checklist.md
│
└── images/
    ├── folder_structure.png
    ├── csv_output_excel.png
    ├── scraping_result_Jupyter.png
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
| 1 | `folder_structure.png` | ✅ Available | Project folder structure in VS Code |
| 2 | `csv_output_excel.png` | ✅ Available | Exported CSV file opened in Excel |
| 3 | `scraping_result_Jupyter.png` | ✅ Available | Scraping results displayed in Jupyter Notebook |
| 4 | `Function to extract Product Title.png` | ✅ Available | Title extraction using `soup.find("span", attrs={"id":'productTitle'})` |
| 5 | `Function to extract Product Price.png` | ✅ Available | Price extraction using `soup.find("span", attrs={'id':'priceblock_ourprice'})` |
| 6 | `Function to extract Product Rating.png` | ✅ Available | Rating extraction using `soup.find("i", attrs={'class':'a-icon a-icon-star'})` |
| 7 | `Function to extract Number of User Reviews.png` | ✅ Available | Review count extraction using `soup.find("span", attrs={'id':'acrCustomerReviewText'})` |
| 8 | `Function to extract Availability Status.png` | ✅ Available | Availability extraction using `soup.find("div", attrs={'id':'availability'})` |

### Screenshot by Category

#### Project Structure (1 image)

| Filename | Description |
|----------|-------------|
| `folder_structure.png` | Complete project folder structure in VS Code |

#### Extraction Functions (5 images)

| Filename | Description |
|----------|-------------|
| `Function to extract Product Title.png` | Extract product title using `#productTitle` selector |
| `Function to extract Product Price.png` | Extract product price using `#priceblock_ourprice` or `#priceblock_dealprice` |
| `Function to extract Product Rating.png` | Extract product rating using `.a-icon-star` or `.a-icon-alt` |
| `Function to extract Number of User Reviews.png` | Extract review count using `#acrCustomerReviewText` |
| `Function to extract Availability Status.png` | Extract availability using `#availability` |

#### Results (2 images)

| Filename | Description |
|----------|-------------|
| `scraping_result_Jupyter.png` | Final scraping results in Jupyter Notebook |
| `csv_output_excel.png` | Exported CSV data viewed in Excel |

### Screenshot Summary

| Category | Count | Files |
|----------|-------|-------|
| Project Structure | 1 | `folder_structure.png` |
| Extraction Functions | 5 | Title, Price, Rating, Reviews, Availability |
| Results | 2 | Jupyter output, CSV output |
| **Total** | **8** | All available in `images/` directory |

---

## Implementation Details

### Import Libraries

```python
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
```

### HTTP Request Configuration

```python
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/114.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US, en;q=0.5'
}
```

### Extraction Functions

```python
# IMAGE: images/Function to extract Product Title.png
def get_title(soup):
    """Extract product title from BeautifulSoup object."""
    try:
        title = soup.find("span", attrs={"id": 'productTitle'})
        title_value = title.text
        title_string = title_value.strip()
    except AttributeError:
        title_string = ""
    return title_string

# IMAGE: images/Function to extract Product Price.png
def get_price(soup):
    """Extract product price from BeautifulSoup object."""
    try:
        price = soup.find("span", attrs={'id': 'priceblock_ourprice'}).string.strip()
    except AttributeError:
        try:
            price = soup.find("span", attrs={'id': 'priceblock_dealprice'}).string.strip()
        except:
            price = ""
    return price

# IMAGE: images/Function to extract Product Rating.png
def get_rating(soup):
    """Extract product rating from BeautifulSoup object."""
    try:
        rating = soup.find("i", attrs={'class': 'a-icon a-icon-star a-star-4-5'}).string.strip()
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class': 'a-icon-alt'}).string.strip()
        except:
            rating = ""
    return rating

# IMAGE: images/Function to extract Number of User Reviews.png
def get_review_count(soup):
    """Extract number of user reviews from BeautifulSoup object."""
    try:
        review_count = soup.find("span", attrs={'id': 'acrCustomerReviewText'}).string.strip()
    except AttributeError:
        review_count = ""
    return review_count

# IMAGE: images/Function to extract Availability Status.png
def get_availability(soup):
    """Extract availability status from BeautifulSoup object."""
    try:
        available = soup.find("div", attrs={'id': 'availability'})
        available = available.find("span").string.strip()
    except AttributeError:
        available = "Not Available"
    return available
```

### Main Scraping Logic

```python
if __name__ == '__main__':
    
    # Search URL
    URL = "https://www.amazon.com/s?k=playstation+4&ref=nb_sb_noss_2"
    
    # HTTP Request to search page
    webpage = requests.get(URL, headers=HEADERS)
    soup = BeautifulSoup(webpage.content, "html.parser")
    
    # Extract product links from search results
    links = soup.find_all("a", attrs={'class': 'a-link-normal s-no-outline'})
    links_list = []
    for link in links:
        links_list.append(link.get('href'))
    
    # Initialize data dictionary
    d = {"title": [], "price": [], "rating": [], "reviews": [], "availability": []}
    
    # Scrape each product
    for link in links_list:
        new_webpage = requests.get("https://www.amazon.com" + link, headers=HEADERS)
        new_soup = BeautifulSoup(new_webpage.content, "html.parser")
        
        d['title'].append(get_title(new_soup))
        d['price'].append(get_price(new_soup))
        d['rating'].append(get_rating(new_soup))
        d['reviews'].append(get_review_count(new_soup))
        d['availability'].append(get_availability(new_soup))
    
    # Create DataFrame and clean
    amazon_df = pd.DataFrame.from_dict(d)
    amazon_df['title'].replace('', np.nan, inplace=True)
    amazon_df = amazon_df.dropna(subset=['title'])
    
    # Export to CSV
    amazon_df.to_csv("amazon_data.csv", header=True, index=False)
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
| Rate Limiting | Add delays between requests |
| Amazon Detection | Rotate User-Agent headers |

---

## Performance Specifications

| Metric | Value |
|--------|-------|
| Products per run | Varies (based on search results) |
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

*Last Updated: 2026-07-20*


**Built with industry-standard data engineering tools**