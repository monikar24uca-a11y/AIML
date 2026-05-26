# Feature Engineering AI Program

import pandas as pd

# Sample dataset
data = {
    "Name": ["Monika", "Rahul", "Kavi"],
    "Math": [80, 75, 90],
    "Science": [85, 70, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Create new feature: Total Marks
df["Total"] = df["Math"] + df["Science"]

# Create new feature: Average Marks
df["Average"] = df["Total"] / 2

# Create new feature: Grade
df["Grade"] = df["Average"].apply(
    lambda x: "A" if x >= 90 else
              "B" if x >= 75 else
              "C"
)

print("\nDataset After Feature Engineering:\n")
print(df)