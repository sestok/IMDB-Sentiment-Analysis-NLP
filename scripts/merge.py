import os

# Directory containing individual text files
directory = 'data/positive_reviews'

# List to store combined reviews
combined_reviews = []

# Iterate through text files in the directory
for filename in os.listdir(directory):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory, filename)
        with open(file_path, 'r', encoding='utf-8') as file:
            review = file.read()
            combined_reviews.append(review)

# Save combined reviews to a single file
with open('combined_positive_reviews.txt', 'w', encoding='utf-8') as file:
    for review in combined_reviews:
        file.write(review + '\n')