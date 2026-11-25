import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

books = []

for page_num in range(1, 4):
    url = f"http://books.toscrape.com/catalogue/page-{page_num}.html"
    print(f"Scraping Page {page_num}...")
    
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        items = soup.find_all("article", class_="product_pod")
        
        for item in items:
            title = item.h3.a["title"]
            
            # Cleanly extract only the digits and dot (e.g., '51.77')
            price_raw = item.find("p", class_="price_color").text
            price_match = re.search(r"\d+\.\d+", price_raw)
            price = float(price_match.group()) if price_match else 0.0
            
            # Rating
            rating_classes = item.find("p", class_="star-rating")["class"]
            rating = rating_classes[1] if len(rating_classes) > 1 else "None"
            
            # Stock availability
            availability = item.find("p", class_="instock availability").text.strip()
            
            books.append({
                "Title": title,
                "Price_GBP": price,
                "Star_Rating": rating,
                "Stock_Status": availability
            })
    else:
        print(f"Failed to load Page {page_num}")

# Save to CSV
df = pd.DataFrame(books)
df.to_csv("books_scraped.csv", index=False)

print("\n--- TASK 1 COMPLETE ---")
print(f"Total rows scraped: {len(df)}")
print("File saved successfully as 'books_scraped.csv'!")
print(df.head())