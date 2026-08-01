import pandas as pd
import numpy as np

df = pd.read_csv("major-cities-in-pakistan-by-population.csv")
print("Columns in dataset:\n")
print(df.columns)
df["Change"] = df["Change"].astype(str).str.replace("%","",regex=False)
df["Change"] = pd.to_numeric(df["Change"], errors="coerce")
smallest_cities = df.nsmallest(5, "Population 2017 Census")

print("1. Five Smallest Major Cities by Population")
print(smallest_cities[["City", "Population 2017 Census"]])

avg_growth = df.groupby("Province")["Change"].mean()
highest_province = avg_growth.idxmax()
highest_growth = avg_growth.max()

print("\n2. Province with Highest Average Growth Rate\n")
print(highest_province, "(", round(highest_growth, 2), "%)")

million_cities = np.sum(df["Population 2017 Census"] > 1000000)

print("\n3. Number of Cities Above 1 Million Population\n")
print("Number of Cities Above 1 Million Population=", million_cities)

mean_population = np.mean(df["Population 2017 Census"])
median_population = np.median(df["Population 2017 Census"])
difference = mean_population - median_population

print("\n4. Mean vs Median Population")
print("Mean Population   =", mean_population)
print(f"Median Population =", median_population)
print("Difference        =", round(difference, 2))

print("\nExplanation:")
print("The mean is much higher than the median because a few very large cities such as Karachi and Lahore increase the average, while most cities have much smaller populations.")