# Random Forest AI Program

import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Sample dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Pass":  [0, 0, 0, 1, 1, 1]
}

# Create DataFrame
df = pd.DataFrame(data)

# Input and Output
X = df[["Hours"]]
y = df["Pass"]

# Create Random Forest model
model = RandomForestClassifier(n_estimators=10)

# Train model
model.fit(X, y)

# Predict result
prediction = model.predict([[4]])

print("Prediction for 4 Hours Study:")
print(prediction[0])