# CodeAlpha Data Analytics Internship

End-to-end Data Analytics project completed during my virtual internship at **CodeAlpha**, covering automated web scraping, exploratory data analysis (EDA), and statistical visualization.

## Project Structure

* `task1_scraper.py` – Python web scraping script extracting book titles, prices (£), star ratings, and stock status across multiple pages from `books.toscrape.com`.
* `books_scraped.csv` – Cleaned dataset containing 60 book records generated from Task 1.
* `task2_eda.py` – Exploratory Data Analysis script auditing data integrity, null values, summary statistics, and categorical distributions.
* `task3_visualization.py` – Data visualization script generating high-resolution statistical charts using Matplotlib and Seaborn.
* `chart1_price_distribution.png` – Histogram with KDE showing book price distribution and mean benchmark (£35.00).
* `chart2_rating_distribution.png` – Bar chart displaying book inventory count across star ratings.
* `chart3_price_by_rating_boxplot.png` – Box plot comparing price ranges across star rating tiers.

## Tech Stack
* **Language:** Python
* **Libraries:** `requests`, `BeautifulSoup (bs4)`, `re`, `pandas`, `matplotlib`, `seaborn`

## Key Analytical Insights
* **Data Integrity:** 60 rows and 4 columns with zero missing values.
* **Pricing:** Average price is **£35.00** (Median: £33.49), ranging from **£12.84** to **£57.31**.
* **Ratings & Stock:** 100% of sampled books are in stock; `One Star` (15) and `Five Stars` (14) represent the largest rating segments, with median prices remaining consistent across rating tiers.