# AI Python Program to Handle Missing Values

import pandas as pd
import numpy as np

# Create sample dataset
data = {
    "Name": ["Monika", "Rahul", None, "Kavi"],
    "Age": [20, np.nan, 22, 21],
    "Marks": [85, 90, np.nan, 88]
}

# Convert into DataFrame
df = pd.DataFrame(data)

# Show original data
print("Original Data:\n")
print(df)

# Check missing values
print("\nMissing Values Count:\n")
print(df.isnull().sum())

# Handle missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Show cleaned data
print("\nData After Handling Missing Values:\n")
print(df)