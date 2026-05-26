# AI Data Analysis Program using Pandas

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load dataset
# Replace with your CSV file
data = pd.read_csv("data.csv")

# Display first rows
print("First 5 Rows:")
print(data.head())

# Dataset information
print("\nDataset Info:")
print(data.info())

# Statistical summary
print("\nStatistical Summary:")
print(data.describe())

# Handle missing values
data = data.dropna()

# Example:
# Assume last column is target variable
X = data.iloc[:, :-1]
y = data.iloc[:, -1]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train AI model
model = LinearRegression()
model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, predictions)

print("\nModel Training Complete")
print("Mean Squared Error:", mse)

# Show predictions
results = pd.DataFrame({
    "Actual": y_test,
    "Predicted": predictions
})

print("\nPrediction Results:")
print(results.head())