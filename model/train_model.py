import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

data = pd.read_csv('data/dataset.csv')

x = data['review']
y = data['sentiment']

vectorizer = CountVectorizer()

x_vec = vectorizer.fit_transform(x)

x_train,x_test,y_train,y_test = train_test_split(x_vec,y,test_size=0.2,random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(x_train,y_train)

pickle.dump(model,open("model/sentiment_model.pkl","wb"))
pickle.dump(vectorizer,open("model/vectorizer.pkl","wb"))

print("model train and save!")