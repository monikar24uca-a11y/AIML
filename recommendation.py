# Simple Recommendation System AI Program

from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

# Sample user-item rating data
data = {
    'Movie1': [5, 4, 0, 1],
    'Movie2': [4, 0, 0, 1],
    'Movie3': [1, 1, 0, 5],
    'Movie4': [0, 0, 5, 4],
    'Movie5': [0, 1, 5, 4]
}

# Create DataFrame
ratings = pd.DataFrame(data,
                       index=['User1', 'User2', 'User3', 'User4'])

print("User Ratings:")
print(ratings)

# Calculate similarity
similarity = cosine_similarity(ratings)

# Convert to DataFrame
similarity_df = pd.DataFrame(similarity,
                             index=ratings.index,
                             columns=ratings.index)

print("\nUser Similarity Matrix:")
print(similarity_df)

# Recommend similar users
user = 'User1'

print(f"\nRecommended similar users for {user}:")
print(similarity_df[user].sort_values(ascending=False))