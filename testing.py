# Create Training and Testing Dataset

import pandas as pd
from sklearn.model_selection import train_test_split

# Sample dataset
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 50, 70, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[["Hours"]]
y = df["Marks"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Display results
print("Training Data:")
print(X_train)

print("\nTesting Data:")
print(X_test)