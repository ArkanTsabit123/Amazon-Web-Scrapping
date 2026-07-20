# amazon_scrape_final.py
"""
Amazon Web Scraping - Final Scraper

This module scrapes product data from Amazon search results using undetected-chromedriver.
Extracts: Title, Price, Rating, Reviews, Availability.

Usage:
    python amazon_scrape_final.py

Output:
    amazon_all_products.csv
"""

from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import time
import random
from typing import Dict, List, Optional, Tuple
import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ============================================
# CONFIGURATION
# ============================================

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

DEFAULT_MAX_PRODUCTS: int = 5
DEFAULT_HEADLESS: bool = False


def get_request_headers() -> Dict[str, str]:
    """Generate random headers to avoid detection."""
    headers = BASE_HEADERS.copy()
    headers['User-Agent'] = random.choice(USER_AGENTS)
    return headers


# ============================================
# BROWSER DRIVER SETUP
# ============================================

def get_driver(headless: bool = False) -> uc.Chrome:
    """
    Setup undetected ChromeDriver to avoid bot detection.

    Args:
        headless: Run browser in headless mode

    Returns:
        uc.Chrome: ChromeDriver instance
    """
    options = uc.ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-features=VizDisplayCompositor")
    options.add_argument("--disable-extensions")

    if headless:
        options.add_argument("--headless=new")

    driver = uc.Chrome(options=options, version_main=150)
    return driver


def fetch_page_selenium(url: str, driver: uc.Chrome, wait_time: int = 10) -> BeautifulSoup:
    """
    Fetch HTML using Selenium with undetected-chromedriver.

    Args:
        url: URL to access
        driver: ChromeDriver instance
        wait_time: Maximum wait time in seconds

    Returns:
        BeautifulSoup: Parsed HTML
    """
    driver.get(url)
    time.sleep(random.uniform(3, 5))

    WebDriverWait(driver, wait_time).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )

    html = driver.page_source
    return BeautifulSoup(html, 'html.parser')


# ============================================
# SELECTORS CONFIGURATION
# ============================================

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


# ============================================
# HELPER FUNCTIONS
# ============================================

def find_element(soup: BeautifulSoup, selectors: List) -> Optional[BeautifulSoup]:
    """Find HTML element using multiple selectors."""
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
    """Extract text from element or return default value."""
    if element:
        text = element.get_text().strip()
        return text if text else default
    return default


# ============================================
# EXTRACTION FUNCTIONS
# ============================================

def extract_title(soup: BeautifulSoup) -> str:
    """Extract product title from BeautifulSoup object."""
    element = find_element(soup, TITLE_SELECTORS)
    return get_text(element)


def extract_price(soup: BeautifulSoup) -> str:
    """Extract product price from BeautifulSoup object."""
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
    """Extract product rating from BeautifulSoup object."""
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
    """Extract number of user reviews from BeautifulSoup object."""
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
    """Extract availability status from BeautifulSoup object."""
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


# ============================================
# PRODUCT SCRAPER
# ============================================

def extract_product_links(soup: BeautifulSoup) -> List[str]:
    """Extract product detail page links from search results."""
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


def scrape_product_page(product_url: str, driver: uc.Chrome) -> Optional[Dict[str, str]]:
    """Scrape a single product page using Selenium."""
    time.sleep(random.uniform(2, 4))
    soup = fetch_page_selenium(product_url, driver)

    if not soup:
        return None

    return {
        'title': extract_title(soup),
        'price': extract_price(soup),
        'rating': extract_rating(soup),
        'reviews': extract_review_count(soup),
        'availability': extract_availability(soup),
    }


# ============================================
# FILTER AVAILABILITY
# ============================================

def filter_available_products(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Filter out products that cannot be shipped to your location."""
    unavailable_keywords = [
        'cannot be shipped to your selected',
        'not available',
        'unavailable'
    ]

    mask = dataframe['availability'].str.lower().str.contains(
        '|'.join(unavailable_keywords),
        case=False,
        na=False
    )

    return dataframe[~mask]


# ============================================
# SCRAPER ENGINE
# ============================================

def scrape_amazon_products(
    search_keyword: str = "playstation 5",
    max_products: int = 10,
    headless: bool = False
) -> pd.DataFrame:
    """
    Scrape Amazon products using undetected-chromedriver.

    Args:
        search_keyword: Keyword to search for
        max_products: Maximum number of products to scrape
        headless: Run browser in headless mode

    Returns:
        pd.DataFrame: Scraped product data
    """
    print(f"Searching for: {search_keyword}")
    print(f"Max products: {max_products}\n")

    driver = get_driver(headless=headless)

    try:
        encoded_keyword = search_keyword.replace(' ', '+')
        search_url = f"https://www.amazon.com/s?k={encoded_keyword}&ref=nb_sb_noss_2"
        print(f"URL: {search_url}\n")

        soup = fetch_page_selenium(search_url, driver)

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

            product_data = scrape_product_page(product_url, driver)

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

        df = filter_available_products(df)
        df.index = range(1, len(df) + 1)

        print(f"\nScraping complete! Saved {len(df)} products")
        return df

    finally:
        driver.quit()


# ============================================
# EXPORT & SUMMARY
# ============================================

def export_to_csv(dataframe: pd.DataFrame, filename: str = 'amazon_data.csv') -> None:
    """Export DataFrame to CSV file."""
    if dataframe.empty:
        print("No data to export")
        return

    dataframe.to_csv(filename, index=False)
    print(f"Exported to {filename}")


def print_summary(dataframe: pd.DataFrame) -> None:
    """Print summary statistics of scraped data."""
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


# ============================================
# COMBINE SCRAPED DATA
# ============================================

def combine_scraped_data(dataframes: List[pd.DataFrame]) -> pd.DataFrame:
    """Combine multiple DataFrames into a single DataFrame."""
    if not dataframes:
        print("No data available")
        return pd.DataFrame()

    combined_df = pd.concat(dataframes, ignore_index=True)
    combined_df.index = range(1, len(combined_df) + 1)

    print(f"\n{'='*60}")
    print(f"Total products scraped: {len(combined_df)}")
    print(f"{'='*60}")

    return combined_df


# ============================================
# MULTI-PRODUCT SCRAPER
# ============================================

def scrape_multiple_products(
    keywords: List[str],
    max_products: int = DEFAULT_MAX_PRODUCTS,
    headless: bool = DEFAULT_HEADLESS
) -> pd.DataFrame:
    """Scrape multiple products with Selenium."""
    all_data = []

    for keyword in keywords:
        print(f"\n{'='*60}")
        print(f"Scraping: {keyword}")
        print(f"{'='*60}\n")

        product_df = scrape_amazon_products(
            search_keyword=keyword,
            max_products=max_products,
            headless=headless
        )

        if not product_df.empty:
            product_df['keyword'] = keyword
            all_data.append(product_df)
            print(f"Success: {keyword} - {len(product_df)} products found")
        else:
            print(f"Failed: {keyword} - No products found")

        time.sleep(5)

    return combine_scraped_data(all_data)


# ============================================
# MAIN
# ============================================

if __name__ == "__main__":
    print("\n" + "="*60)
    print("AMAZON WEB SCRAPING - FINAL SCRAPER")
    print("="*60 + "\n")

    scraped_data = scrape_multiple_products(
        keywords=POPULAR_PRODUCTS[:3],
        max_products=3,
        headless=False
    )

    if not scraped_data.empty:
        print("\nScraped Data:")
        print(scraped_data.to_string())
        export_to_csv(scraped_data, 'amazon_all_products.csv')
        print_summary(scraped_data)
    else:
        print("No data was successfully scraped")