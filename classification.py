# Import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Sample text data
texts = [
    "I love this product",
    "This is an amazing movie",
    "I hate this service",
    "The food was terrible",
    "Very happy with the experience",
    "Worst app ever"
]

# Labels (Positive = 1, Negative = 0)
labels = [1, 1, 0, 0, 1, 0]

# Convert text into numerical features
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

# Split data into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, labels, test_size=0.2, random_state=42
)

# Create model
model = MultinomialNB()

# Train model
model.fit(X_train, y_train)

# Predict test data
y_pred = model.predict(X_test)

# Check accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))

# Predict new text
new_text = ["I really like this app"]
new_X = vectorizer.transform(new_text)

prediction = model.predict(new_X)

if prediction[0] == 1:
    print("Positive Text")
else:
    print("Negative Text")