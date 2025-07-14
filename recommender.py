import pandas as pd

# Load your dataset
books_df = pd.read_csv("data/books.csv")

def recommend_books(preference):
    # Filter by genre (simple example)
    filtered = books_df[books_df['genre'].str.contains(preference, case=False, na=False)]
    return filtered['title'].head(5).tolist()
