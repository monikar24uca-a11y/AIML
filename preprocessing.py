# Data Preprocessing AI Program

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Sample dataset
data = {
    "Name": ["Monika", "Rahul", None, "Kavi"],
    "Age": [20, np.nan, 22, 21],
    "Marks": [85, 90, np.nan, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Handle missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Convert text data into numbers
df["Name"] = df["Name"].astype("category").cat.codes

# Normalize numerical data
scaler = MinMaxScaler()

df[["Age", "Marks"]] = scaler.fit_transform(df[["Age", "Marks"]])

print("\nPreprocessed Dataset:\n")
print(df)