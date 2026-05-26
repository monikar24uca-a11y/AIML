# Simple Feature Engineering AI Program

import pandas as pd

# Sample data
data = {
    "Math": [80, 70, 90],
    "Science": [85, 75, 95]
}

# Create DataFrame
df = pd.DataFrame(data)

# Create new feature
df["Total"] = df["Math"] + df["Science"]

# Show result
print(df)