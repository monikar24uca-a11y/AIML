# Text Preprocessing AI Program

import nltk
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Input text
text = "Hello! This is an AI text preprocessing example."

# Convert to lowercase
text = text.lower()

# Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Tokenization
tokens = word_tokenize(text)

# Remove stopwords
stop_words = set(stopwords.words('english'))
filtered_words = [word for word in tokens if word not in stop_words]

# Display results
print("Original Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nFiltered Words:")
print(filtered_words)