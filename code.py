# Netflix Dataset Analysis using Dask with Visualizations

import dask.dataframe as dd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

# Load the dataset
df = dd.read_csv("netflix.csv", sep=';', quotechar='"', assume_missing=True)

# Drop rows with null 'type'
df = df.dropna(subset=['type'])

# Null value summary
print("\n🔍 Null Values:")
print(df.isnull().sum().compute())

# Type count
type_counts = df['type'].value_counts().compute()
print("\n🎬 Type Distribution:")
print(type_counts)

# Plot type distribution
type_counts.plot(kind='bar', color='skyblue')
plt.title('Count of Content Types')
plt.xlabel('Type')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig("type_distribution.png")
plt.clf()

# Top countries
top_countries = df['country'].value_counts().nlargest(10).compute()
print("\n🌍 Top 10 Countries by Content:")
print(top_countries)

top_countries.plot(kind='barh', color='salmon')
plt.title('Top 10 Countries by Netflix Content')
plt.xlabel('Number of Titles')
plt.tight_layout()
plt.savefig("top_countries.png")
plt.clf()

# Yearly trend
df['date_added'] = dd.to_datetime(df['date_added'], errors='coerce')
df['year_added'] = df['date_added'].dt.year
yearly_add = df['year_added'].value_counts().sort_index().compute()
print("\n📅 Content Added Per Year:")
print(yearly_add)

yearly_add.plot(kind='line', marker='o', color='green')
plt.title('Content Added to Netflix Per Year')
plt.xlabel('Year')
plt.ylabel('Number of Titles')
plt.tight_layout()
plt.savefig("content_per_year.png")
plt.clf()

# Genre analysis
df['listed_in'] = df['listed_in'].fillna('')
genres = df['listed_in'].str.split(', ')
genres = genres.explode()
top_genres = genres.value_counts().nlargest(10).compute()
print("\n🎭 Top 10 Genres:")
print(top_genres)

top_genres.plot(kind='bar', color='purple')
plt.title('Top 10 Netflix Genres')
plt.xlabel('Genre')
plt.ylabel('Frequency')
plt.tight_layout()
plt.savefig("top_genres.png")
plt.clf()

print("\n✅ Analysis Complete. Charts saved as PNG images.")
