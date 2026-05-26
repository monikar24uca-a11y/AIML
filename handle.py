import pandas as pd
import numpy as np

# Sample data with missing values
data = {
    "Name": ["Monika", "Rahul", "Kavi", None],
    "Age": [20, np.nan, 22, 21],
    "Marks": [85, 90, np.nan, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Check missing values
print("\nMissing Values:")
print(df.isnull())

# Count missing values
print("\nTotal Missing Values:")
print(df.isnull().sum())

# Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(0, inplace=True)
df["Name"].fillna("Unknown", inplace=True)

print("\nAfter Handling Missing Values:")
print(df)