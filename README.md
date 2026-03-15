# AI Sentiment Analysis Dashboard

![Python](https://img.shields.io/badge/Python-3.10-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-NLP-orange)

An **AI-powered Sentiment Analysis Web Application** that analyzes text and predicts whether the sentiment is **Positive** or **Negative**.

This project demonstrates a **complete Machine Learning deployment pipeline** using:

- Natural Language Processing (NLP)
- Machine Learning Model Inference
- FastAPI
- Streamlit Interactive Dashboard

---

# Live Demo

Streamlit Dashboard  
https://your-streamlit-render-url.onrender.com

FastAPI API  
[https://your-api-render-url.onrender.com](https://ai-sentiment-analysis-dashboard-rw82.onrender.com)

API Documentation  
[https://your-api-render-url.onrender.com/docs](https://ai-sentiment-analysis-dashboard-rw82.onrender.com)

---

# Demo

![Demo](images/demo.gif)

---

# Screenshot

![Dashboard](images/screenshot.png)

---

# System Architecture

User Input  
↓  
Streamlit Dashboard  
↓  
FastAPI REST API  
↓  
TF-IDF Vectorizer  
↓  
Machine Learning Model  
↓  
Sentiment Prediction

---

# Features

- Real-time sentiment prediction
- FastAPI REST API backend
- Streamlit interactive dashboard
- Sentiment probability visualization
- Word Cloud visualization
- Clean modular project structure

---

# Tech Stack

Python

Machine Learning  
- Scikit-learn  
- Pandas  
- NumPy  

Backend  
- FastAPI  

Frontend  
- Streamlit  

Visualization  
- Matplotlib  
- WordCloud  

---

# Project Structure

ai-sentiment-analysis-dashboard

api  
└── main.py  

dashboard  
└── app.py  

model  
└── sentiment_model.pkl  

data  

images  
├── demo.gif  
└── screenshot.png  

requirements.txt  
README.md

---

# Installation

Clone the repository

git clone https://github.com/wpko/ai-sentiment-analysis-dashboard.git


Navigate into project

cd ai-sentiment-analysis-dashboard


Install dependencies

pip install -r requirements.txt

---

# Run FastAPI Server
uvicorn api.main:app --reload


API will run at
[http://127.0.0.1:8000](https://ai-sentiment-analysis-dashboard-rw82.onrender.com)
API documentation
[http://127.0.0.1:8000/docs](https://ai-sentiment-analysis-dashboard-rw82.onrender.com)/docs

---

# Run Streamlit Dashboard
streamlit run dashboard/app.py
Dashboard will run at
[http://localhost:8501](https://ai-sentiment-analysis-dashboard-streamlit.onrender.com/)

---

# API Example

POST request


POST /predict


Request

```json
{
"text": "This movie is amazing"
}

Response

{
"sentiment": "Positive",
"probability": 0.91
}
Example Prediction

Input

This movie is amazing

Output

Sentiment: Positive
Probability: 0.91

Future Improvements

Deploy with Docker

Add sentiment history database

Improve model using deep learning

Add multi-language sentiment analysis

Add real-time analytics dashboard

Author

Wai Lay

Aspiring Python / AI Developer

GitHub
https://github.com/wpko
