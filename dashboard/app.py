import streamlit as st
import requests
import matplotlib.pyplot as plt
from wordcloud import WordCloud

API_URL = "https://ai-sentiment-analysis-dashboard-rw82.onrender.com/predict"

st.title("AI sentiment Analysis Dashboard")
text_input = st.text_area("Enter text to analyze sentiment")

if st.button("Analyze Sentiment"):
    response = requests.post(API_URL, json={"text":text_input})
    if response.status_code == 200:
        result = response.json()
        sentiment = result['sentiment']
        pos = result['positive_score']
        neg = result['negative_score']
        
        st.subheader("Prediction Result")
        st.write(f"Sentiment: **{sentiment}**")
        
        labels = ['positive','negative']
        values = [pos,neg]
        
        fig,ax = plt.subplots()
        ax.bar(labels,values)
        ax.set_title("Sentiment Probability")
        
        st.pyplot(fig)
        
        wordcloud = WordCloud(width=800,height=400).generate(text_input)
        
        st.subheader("Word Cloud")
        fig2,ax2 = plt.subplots()
        ax2.imshow(wordcloud)
        ax2.axis('off')
        
        st.pyplot(fig2)
        
    else:
        st.error("API error")
