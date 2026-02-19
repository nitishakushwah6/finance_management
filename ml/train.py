import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

data = pd.read_csv("data/kaggle_finance_tickets.csv")

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['text'])

model = LogisticRegression()
model.fit(X, data['urgency'])

pickle.dump(model, open("ml/urgency.pkl", "wb"))
pickle.dump(vectorizer, open("ml/vectorizer.pkl", "wb"))
