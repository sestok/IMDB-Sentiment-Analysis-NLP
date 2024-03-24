from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load preprocessed positive reviews from file
with open('data/positive_reviews.txt', 'r', encoding='utf-8') as file:
    positive_reviews = file.readlines()

# Load preprocessed negative reviews from file
with open('data/negative_reviews.txt', 'r', encoding='utf-8') as file:
    negative_reviews = file.readlines()

# Combine positive and negative labels
y = ['positive'] * len(positive_reviews) + ['negative'] * len(negative_reviews)

# Combine positive and negative reviews into a single list
all_reviews = positive_reviews + negative_reviews

# Initialize CountVectorizer
vectorizer = CountVectorizer()

# Fit and transform the data
X = vectorizer.fit_transform(all_reviews)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Multinomial Naive Bayes classifier
clf = MultinomialNB()

# Train the classifier
clf.fit(X_train, y_train)

# Predict the labels for the test set
y_pred = clf.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
