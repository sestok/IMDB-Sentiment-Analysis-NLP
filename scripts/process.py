import os
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def preprocess_document(document):
    document = document.lower()
    document = document.replace("<br />", " ")
    tokens = word_tokenize(document)
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    # Stemming
    stemmer = PorterStemmer()
    tokens = [stemmer.stem(token) for token in tokens]
    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    
    # Join tokens back into a single string
    processed_document = ' '.join(tokens)
  
    return processed_document
  
def preprocess_directory(directory):
    processed_documents = []
    for filename in os.listdir(directory):
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as file:
            document = file.read()
            processed_document = preprocess_document(document)
            processed_documents.append(processed_document)
    return processed_documents

# Path to the directory containing positive and negative reviews
positive_reviews_directory = 'aclImdb/train/pos'
negative_reviews_directory = 'aclImdb/train/neg'

# Preprocess positive reviews
positive_reviews = preprocess_directory(positive_reviews_directory)

# Preprocess negative reviews
negative_reviews = preprocess_directory(negative_reviews_directory)

# Example: Print the first preprocessed positive review
print("Preprocessed Positive Review:")
print(positive_reviews[0])
