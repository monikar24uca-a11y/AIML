# Sentiment Analysis AI Program

from textblob import TextBlob

# Input text
text = input("Enter a sentence: ")

# Perform sentiment analysis
analysis = TextBlob(text)

# Get polarity
polarity = analysis.sentiment.polarity

# Display result
print("\nPolarity Score:", polarity)

if polarity > 0:
    print("Sentiment: Positive")
elif polarity < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")