import streamlit as st
import numpy as np
import pickle

books_info = pickle.load(open('books.pkl', 'rb'))
pt = pickle.load(open('pt.pkl', 'rb'))
popular_books = pickle.load(open('Popular_books.pkl', 'rb'))
similarity_score = pickle.load(open('similarity_score.pkl', 'rb'))
books_list = books_info["Book-Title"].values
st.title("Book Recommender System")

def recommend(book_name):
     index = np.where(pt.index == book_name)[0][0]
     similar_books = sorted(list(enumerate(similarity_score[index])), key=lambda x: x[1], reverse=True)[1:7]

     recommended_books = []
     for i in similar_books:
          recommended_books.append(pt.index[i[0]])

     return recommended_books

book_name = st.selectbox(
     "Enter a Book",
     books_list)

if st.button('Recommend'):
     recommended_books = recommend(book_name)
     year = []
     publisher = []
     url = []
     author = []
     name = []

     for i in recommended_books:
          year.append("Year of Publication : " + str(books_info[books_info["Book-Title"] == i]["Year-Of-Publication"].values[0]))
          publisher.append("Publisher : " + books_info[books_info["Book-Title"] == i]["Publisher"].values[0])
          url.append(books_info[books_info["Book-Title"] == i]["Image-URL-L"].values[0])
          author.append("Author : " + books_info[books_info["Book-Title"] == i]["Book-Author"].values[0])
          name.append("Name : " + i)

     col1, col2, col3 = st.columns(3)

     with col1:
          st.image(url[0])
          st.text(name[0])
          st.text(author[0])
          st.write(publisher[0])
          st.text(year[0])
          st.text("")
     with col2:
          st.image(url[1])
          st.text(name[1])
          st.text(author[1])
          st.write(publisher[1])
          st.text(year[1])
          st.text("")
     with col3:
          st.image(url[2])
          st.text(name[2])
          st.text(author[2])
          st.write(publisher[2])
          st.text(year[2])
          st.text("")


     col4, col5, col6 = st.columns(3)

     with col4:
          st.image(url[3])
          st.text(name[3])
          st.text(author[3])
          st.write(publisher[3])
          st.text(year[3])
          st.text("")
     with col5:
          st.image(url[4])
          st.text(name[4])
          st.text(author[4])
          st.write(publisher[4])
          st.text(year[4])
          st.text("")
     with col6:
          st.image(url[5])
          st.text(name[5])
          st.text(author[5])
          st.write(publisher[5])
          st.text(year[5])
          st.text("")
else:
     pname = popular_books["Book-Title"].values
     purl = popular_books["Image-URL-L"]
     pauthor = popular_books["Book-Author"].values
     pyear = popular_books["Year-Of-Publication"].values
     ppublisher = popular_books["Publisher"].values
     pnum_rating = popular_books["num_ratings"].values
     pavg_rating = popular_books["avg_ratings"].values

     for i in purl:
          st.image(i)

     col1, col2, col3 = st.columns(3)

     with col1:
          st.image(purl[0])
          st.text(pname[0])
          st.text(pauthor[0])
          st.write(ppublisher[0])
          st.text(pyear[0])
          st.text("")
     with col2:
          st.image(purl[1])
          st.text(pname[1])
          st.text(pauthor[1])
          st.write(ppublisher[1])
          st.text(pyear[1])
          st.text("")
     with col3:
          st.image(purl[2])
          st.text(pname[2])
          st.text(pauthor[2])
          st.write(ppublisher[2])
          st.text(pyear[2])
          st.text("")