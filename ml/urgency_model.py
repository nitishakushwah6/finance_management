import pickle

model = pickle.load(open("ml/urgency.pkl", "rb"))
vectorizer = pickle.load(open("ml/vectorizer.pkl", "rb"))

def predict_urgency(text):
    vec = vectorizer.transform([text])
    return model.predict(vec)[0]
