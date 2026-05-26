# Normalize Dataset AI Program

import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Sample dataset
data = {
    "Age": [20, 25, 30, 35],
    "Marks": [60, 70, 80, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

print("Original Dataset:\n")
print(df)

# Create scaler object
scaler = MinMaxScaler()

# Normalize data
normalized_data = scaler.fit_transform(df)

# Convert back to DataFrame
normalized_df = pd.DataFrame(normalized_data, columns=df.columns)

print("\nNormalized Dataset:\n")
print(normalized_df)