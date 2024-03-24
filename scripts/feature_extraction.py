from sklearn.feature_extraction.text import CountVectorizer

# Combine positive and negative reviews into a single list
all_reviews = positive_reviews + negative_reviews

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the data
X = vectorizer.fit_transform(all_reviews)

# Print the shape of the feature matrix
print("Shape of the feature matrix:", X.shape)