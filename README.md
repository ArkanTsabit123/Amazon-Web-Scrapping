# 🛒 Amazon Web Scraping Project

This project is a web scraping implementation to extract product data from Amazon e-commerce site using Python. Built as part of a Data Engineering portfolio to demonstrate web data extraction capabilities.

## 🎯 Project Objectives

- Extract product data including **title, price, rating, and availability** from Amazon product pages.
- Clean and structure the scraped data.
- Save the data into **CSV format** for further analysis.
- Understand the fundamentals of web scraping and how to handle anti-scraping challenges.

## 🛠️ Tools & Technologies

| Tool | Function |
|------|----------|
| **Python 3.x** | Primary programming language |
| **Requests** | Send HTTP requests to web pages |
| **BeautifulSoup4** | Parse and extract data from HTML |
| **Pandas** | Data manipulation and CSV export |
| **Jupyter Notebook** | Interactive development and experimentation |

## 📁 Project Structure

```
Amazon-Web-Scrapping/
├── amazon_web_scraping_tutorial.ipynb   # Main tutorial notebook
├── amazon_scrape_final.ipynb            # Final scraper version
├── amazon_products.csv                  # Scraping results (generated)
└── README.md                            # Project documentation
```

## 🚀 How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/ArkanTsabit123/Amazon-Web-Scrapping.git
cd Amazon-Web-Scrapping
```

### 2. Install Dependencies

```bash
pip install requests beautifulsoup4 pandas lxml jupyter
```

### 3. Launch Jupyter Notebook

```bash
jupyter notebook amazon_web_scraping_tutorial.ipynb
```

### 4. Follow the Notebook Steps

Run each code cell sequentially. You can replace the product URL with any Amazon product you want to scrape.

## 📊 Sample Scraping Results

Example of data successfully extracted:

| Title | Price | Rating |
|-------|-------|--------|
| Bose QuietComfort 45 | $279.00 | 4.5 out of 5 stars |
| Sony WH-1000XM5 | $398.00 | 4.6 out of 5 stars |
| Apple AirPods Pro 2 | $249.00 | 4.7 out of 5 stars |

## ⚠️ Important Notes

- Amazon has strict **anti-scraping** measures. Use appropriate `User-Agent` headers and add delays (`time.sleep()`) to avoid being blocked.
- This project is for **educational purposes** and personal use only. Respect Amazon's Terms of Service.
- Amazon's HTML structure can change over time, so the code may need adjustments.


## 📈 Future Improvements

- [ ] Scrape multiple product pages
- [ ] Build a price visualization dashboard
- [ ] Add price change notification feature
- [ ] Deploy as a simple API with FastAPI

## 👤 About the Author

**Arkan Tsabit** - Certified Data Engineer (Oracle, IBM, Meta) with expertise in building scalable data pipelines, cloud data warehousing, and real-time streaming solutions. Passionate about turning raw data into actionable insights.

[![GitHub](https://img.shields.io/badge/GitHub-ArkanTsabit123-181717?style=flat&logo=github)](https://github.com/ArkanTsabit123)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-ArkanTsabit-0A66C2?style=flat&logo=linkedin)](https://www.linkedin.com/in/arkan-tsabit-116a2434b)
---

**Happy scraping!** Feel free to reach out if you have any questions. 