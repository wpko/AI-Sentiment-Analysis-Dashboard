from fastapi import FastAPI
from pydantic import BaseModel
import pickle

#load model
model = pickle.load(open("model/sentiment_model.pkl","rb"))
vectorizer = pickle.load(open("model/vectorizer.pkl","rb"))

app = FastAPI()

class TextInput(BaseModel):
    text:str
    
@app.get("/")
def home():
    return {"message":"Sentiment analysis API is running"}

@app.post("/predict")
def predict_sentiment(data: TextInput):
    text = data.text
    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)[0]
    probabilities = model.predict_proba(text_vec)[0]
    
    return{
        "text":text,
        "sentiment":prediction,
        "positive_score":float(probabilities[1]),
        "negative_score":float(probabilities[0])
    }