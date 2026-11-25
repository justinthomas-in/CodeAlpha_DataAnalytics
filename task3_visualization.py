import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load the dataset
df = pd.read_csv("books_scraped.csv")

# Set global visual style
sns.set_theme(style="whitegrid")
plt.rcParams["font.sans-serif"] = "DejaVu Sans"

print("==========================================")
print("     TASK 3: DATA VISUALIZATION           ")
print("==========================================\n")

# -------------------------------------------------------------
# Chart 1: Price Distribution (Histogram with KDE)
# -------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.histplot(df["Price_GBP"], kde=True, color="#2b5c8f", bins=10)
plt.title("Book Price Distribution (in GBP)", fontsize=14, fontweight="bold", pad=12)
plt.xlabel("Price (£)", fontsize=11)
plt.ylabel("Frequency (Number of Books)", fontsize=11)
plt.axvline(df["Price_GBP"].mean(), color="red", linestyle="--", label=f'Mean Price (£{df["Price_GBP"].mean():.2f})')
plt.legend()
plt.tight_layout()
plt.savefig("chart1_price_distribution.png", dpi=300)
print("-> Saved: chart1_price_distribution.png")
plt.close()

# -------------------------------------------------------------
# Chart 2: Star Rating Distribution (Bar Chart)
# -------------------------------------------------------------
rating_order = ["One", "Two", "Three", "Four", "Five"]

plt.figure(figsize=(8, 5))
ax = sns.countplot(data=df, x="Star_Rating", order=rating_order, palette="Blues_r")
plt.title("Inventory Count by Star Rating", fontsize=14, fontweight="bold", pad=12)
plt.xlabel("Star Rating", fontsize=11)
plt.ylabel("Book Count", fontsize=11)

# Annotate count values on top of each bar
for p in ax.patches:
    ax.annotate(f'{int(p.get_height())}', 
                (p.get_x() + p.get_width() / 2., p.get_height()), 
                ha='center', va='bottom', fontsize=11, color="black", 
                xytext=(0, 3), textcoords='offset points')

plt.tight_layout()
plt.savefig("chart2_rating_distribution.png", dpi=300)
print("-> Saved: chart2_rating_distribution.png")
plt.close()

# -------------------------------------------------------------
# Chart 3: Price vs Star Rating (Box Plot)
# -------------------------------------------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x="Star_Rating", y="Price_GBP", order=rating_order, palette="Set2")
plt.title("Price Distribution Across Star Ratings", fontsize=14, fontweight="bold", pad=12)
plt.xlabel("Star Rating", fontsize=11)
plt.ylabel("Price (£)", fontsize=11)
plt.tight_layout()
plt.savefig("chart3_price_by_rating_boxplot.png", dpi=300)
print("-> Saved: chart3_price_by_rating_boxplot.png")
plt.close()

print("\n==========================================")
print("  ALL CHARTS GENERATED & SAVED AS PNG!    ")
print("==========================================")