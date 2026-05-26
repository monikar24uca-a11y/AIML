# Simple Data Preprocessing AI Program

import pandas as pd

# Sample data
data = {
    "Name": ["Monika", None, "Kavi"],
    "Marks": [80, 90, None]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Data:\n")
print(df)

# Handle missing values
df["Name"] = df["Name"].fillna("Unknown")
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print("\nProcessed Data:\n")
print(df)