import pandas as pd

# 1. Load the scraped dataset
df = pd.read_csv("books_scraped.csv")

print("==========================================")
print("       TASK 2: EXPLORATORY DATA ANALYSIS  ")
print("==========================================\n")

# 2. Basic dataset shape and columns
print("--- 1. DATASET OVERVIEW ---")
print(f"Total Rows: {df.shape[0]}")
print(f"Total Columns: {df.shape[1]}")
print("Column Names:", list(df.columns))
print("\nFirst 5 Records:")
print(df.head())

# 3. Data types and missing values
print("\n--- 2. DATA INTEGRITY & MISSING VALUES ---")
print(df.info())
print("\nMissing values per column:")
print(df.isnull().sum())

# 4. Statistical Summary for Price
print("\n--- 3. PRICE ANALYSIS (STATISTICS) ---")
print(df["Price_GBP"].describe())

avg_price = df["Price_GBP"].mean()
min_price = df["Price_GBP"].min()
max_price = df["Price_GBP"].max()

print(f"\nAverage Book Price: £{avg_price:.2f}")
print(f"Cheapest Book Price: £{min_price:.2f}")
print(f"Most Expensive Book Price: £{max_price:.2f}")

# 5. Rating Distribution
print("\n--- 4. STAR RATING DISTRIBUTION ---")
rating_counts = df["Star_Rating"].value_counts()
print(rating_counts)

# 6. Stock Availability Check
print("\n--- 5. STOCK STATUS OVERVIEW ---")
print(df["Stock_Status"].value_counts())

print("\n==========================================")
print("       EDA COMPLETED SUCCESSFULLY!        ")
print("==========================================")
