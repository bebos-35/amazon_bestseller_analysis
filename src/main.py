## Step 1: Import pandas 
import pandas as pd

## Step 2: Read csv file
df = pd.read_csv("bestsellers.csv")

## Step 3: Cleaning of data
# Drop duplicates
df = df.drop_duplicates(inplace=True) # Changes are directly applied to the original dataframe

# Rename columns 
df = df.rename(columns = {"Name": "Title", "Year": "Publication Year", "User Rating": "Rating"}, inplace=True)

# Convert data types 
df["Price"] = df["Price"].astype(float)

## Step 5: Analysis
# Author popularity
author_counts = df["Author"].value_counts()
print(author_counts)

# Average rating by genre
avg_rating_by_genre = df.groupby("Genre")["Rating"].mean()
print(avg_rating_by_genre)

## Step 6: Export the results
# Export top authors
author_counts.head(10).to_csv("top_authors.csv")
# Export average rating by genre
avg_rating_by_genre.to_csv("avg_rating_by_genre.csv")

