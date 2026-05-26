# Spam Detection System AI Program

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'Message': [
        'Win money now',
        'Hello friend',
        'Claim your prize',
        'How are you',
        'Free offer available',
        'Lets meet tomorrow'
    ],
    'Label': [
        'Spam',
        'Ham',
        'Spam',
        'Ham',
        'Spam',
        'Ham'
    ]
}

# Create DataFrame
df = pd.DataFrame(data)

# Convert text into numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df['Message'])

# Labels
y = df['Label']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Test with new message
msg = ["Free cash prize"]
msg_vector = vectorizer.transform(msg)

prediction = model.predict(msg_vector)

print("\nMessage:", msg[0])
print("Prediction:", prediction[0])