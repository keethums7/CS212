from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import numpy as np


def main():
    # fetch the training data (limit to 4)
    categories = ['alt.atheism', 'soc.religion.christian', 'comp.graphics', 'sci.med']
    ml_train = fetch_20newsgroups(subset='train', categories=categories, shuffle=True, random_state=42)

    # build a feature vector matrix
    count_vectorizer = CountVectorizer()
    ml_train_counts = count_vectorizer.fit_transform(ml_train.data)

    # use a term frequency transformer to keep docs of different lengths comparable
    tfidf_transformer = TfidfTransformer()
    ml_train_tfidf = tfidf_transformer.fit_transform(ml_train_counts)

    # training a classifier on the data
    ml_classifier = MultinomialNB().fit(ml_train_tfidf, ml_train.target)

    # test classifier on a dedicated test subset of the data
    ml_test = fetch_20newsgroups(subset='test', categories=categories, shuffle=True, random_state=42)

    # new feature vector matrix and term frequency matrix for the test data
    # using transform instead of fit_transform to use the same vectorizer and transformer as the training data
    ml_test_counts = count_vectorizer.transform(ml_test.data)
    ml_test_tfidf = tfidf_transformer.transform(ml_test_counts)

    # make predictions on the test data
    ml_test_prediction = ml_classifier.predict(ml_test_tfidf)

    # print the predicted categories for each document in the test set
    for doc, category in zip(ml_test.data, ml_test_prediction):
        print(f"Predicted category: {ml_test.target_names[category]}")


    ml_accuracy_prediction = ml_classifier.predict(ml_test_tfidf)
    ml_accuracy = np.mean(ml_accuracy_prediction == ml_test.target)

    print(f"\nAccuracy of the classifier on the test set: {ml_accuracy * 100:.2f}%")

    # print the accuracy of the classifier on the test set
if __name__ == "__main__":
    main()
