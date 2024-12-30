import streamlit as st
import pandas as pd
import sklearn
import numpy as np
import pickle
import scipy

books = pd.read_csv('BX_Books.csv', sep = ';', encoding='latin-1')

def recommend(Selected_Book_Name):
    for i in range(0,len(book_pivot)):
        if book_pivot.index[i] == Selected_Book_Name:
            distances, suggestions = model.kneighbors(book_pivot.iloc[i, :].values.reshape(1,-1), n_neighbors=6)
    recommended_urls = []
    for i in range(len(suggestions)):
        for j in books['Book-Title']:
            if (j == book_pivot.index[suggestions[i]]).any():
                x = books[books['Book-Title'] == j]['Image-URL-M'].reset_index()
                x.drop(columns = 'index', inplace = True)
                if x['Image-URL-M'][0] not in recommended_urls:
                    recommended_urls.append(x['Image-URL-M'][0])          
                
    return suggestions, recommended_urls

model = pickle.load(open('Model.pkl','rb'))
df = pickle.load(open('data.pkl','rb'))
book_pivot = pickle.load(open('book_pivot.pkl','rb'))

book_names = df['title'].unique()

st.header('Book recommender System')
Selected_Book_Name = st.selectbox(
"Which book have you read?",
book_names
)

if st.button('Show Recommendation'):
    recommended_books, recommended_urls = recommend(Selected_Book_Name)
    recommended_books = recommended_books.flatten().tolist()
    for i in range(1, len(recommended_books)):
        st.text(book_pivot.index[recommended_books[i]])
        st.image(recommended_urls[i])
        