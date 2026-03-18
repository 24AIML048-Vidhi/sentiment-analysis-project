import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from clean import clean_text


def train_model():

    # load dataset
    data = pd.read_csv("data.csv")

    # clean text
    data["Text"] = data["Text"].apply(clean_text)

    # convert text to numbers
    cv = CountVectorizer()

    X = cv.fit_transform(data["Text"])
    y = data["Sentiment"]

    # split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # train model
    model = LogisticRegression()

    model.fit(X_train, y_train)

    # test accuracy
    pred = model.predict(X_test)

    print("Accuracy:", accuracy_score(y_test, pred))

    # return model + vectorizer
    return model, cv