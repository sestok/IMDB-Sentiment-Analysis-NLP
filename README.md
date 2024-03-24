# Sentiment Analysis in NLP

## Overview
This project implements sentiment analysis in natural language processing (NLP) using machine learning techniques. The goal is to classify movie reviews as positive or negative based on the sentiment expressed in the text.

## Features
- Preprocesses raw text data to remove noise and standardize the format.
- Extracts features from text data using Bag-of-Words (BoW) representation.
- Trains a sentiment analysis model using Multinomial Naive Bayes classifier.
- Evaluates the model's performance using accuracy as the evaluation metric.

## Dataset
The IMDb Movie Reviews dataset is used for training and testing the sentiment analysis model. The dataset consists of positive and negative movie reviews.


## Instructions
1. **Data Preprocessing**: 
   - Ensure that the IMDb Movie Reviews dataset is downloaded and stored in the `data` directory.
   - Preprocess the raw text data to clean and standardize it before feature extraction.

2. **Feature Extraction**:
   - Run the `feature_extraction.py` script to convert text data into numerical feature vectors using Bag-of-Words representation.

3. **Model Building**:
   - Run the `model_building.py` script to train the sentiment analysis model using the preprocessed data and evaluate its performance.

4. **Interpret Results**:
   - Analyze the accuracy of the model and review any misclassifications to iteratively improve the model's performance.

## Dependencies
- Python 3.x
- scikit-learn
- Other dependencies (if any)

## Usage
1. Clone the repository:
`git clone https://github.com/sestok/IMDB-Sentiment-Analysis-NLP/`
2. Download the Dataset from here https://ai.stanford.edu/~amaas/data/sentiment/
3. Navigate to the project directory:
`cd Sentiment-Analysis-in-NLP`
4. Follow the instructions provided above to preprocess the data, extract features, and build the sentiment analysis model.
