# Linear Regression AI Program

import pandas as pd
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    "Hours": [1, 2, 3, 4, 5],
    "Marks": [20, 40, 50, 70, 90]
}

# Create DataFrame
df = pd.DataFrame(data)

# Input and Output
X = df[["Hours"]]
y = df["Marks"]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Predict output
prediction = model.predict([[6]])

print("Predicted Marks for 6 Hours Study:")
print(prediction[0])