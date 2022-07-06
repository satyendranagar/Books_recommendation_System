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
          st.text(publisher[3])
          st.text(year[3])
          st.text("")
     with col5:
          st.image(url[4])
          st.text(name[4])
          st.text(author[4])
          st.text(publisher[4])
          st.text(year[4])
          st.text("")
     with col6:
          st.image(url[5])
          st.text(name[5])
          st.text(author[5])
          st.text(publisher[5])
          st.text(year[5])
          st.text("")
else:
     name = popular_books["Book-Title"].values
     url = popular_books["Image-URL-L"]
     author = popular_books["Book-Author"].values
     year = popular_books["Year-Of-Publication"].values
     publisher = popular_books["Publisher"].values
     num_rating = popular_books["num_ratings"].values
     avg_rating = popular_books["avg_ratings"].values
	col1, col2, col3, col4, col5 = st.columns(5)
	
	for i in range(10):

     	with col1:
          	st.image(url[i*5 + 0])
          	st.text("Name : " + name[i*5 + 0])
          	st.text("Author : " + author[i*5 + 0])
          	st.text("Publisher : " + publisher[i*5 + 0])
          	st.text("Year : " + str(year[i*5 + 0]))
			st.text("Num_rating : " + str(num_rating[i*5 + 0]))
			st.text("Avg_rating : " + str(avg_rating[i*5 + 0]))
          	st.text("")
		
		with col2:
          	st.image(url[i*5 + 1])
          	st.text("Name : " + name[i*5 + 1])
          	st.text("Author : " + author[i*5 + 1])
          	st.text("Publisher : " + publisher[i*5 + 1])
          	st.text("Year : " + str(year[i*5 + 1]))
			st.text("Num_rating : " + str(num_rating[i*5 + 1]))
			st.text("Avg_rating : " + str(avg_rating[i*5 + 1]))
          	st.text("")
			
		with col3:
          	st.image(url[i*5 + 2])
          	st.text("Name : " + name[i*5 + 2])
          	st.text("Author : " + author[i*5 + 2])
          	st.text("Publisher : " + publisher[i*5 + 2])
          	st.text("Year : " + str(year[i*5 + 2]))
			st.text("Num_rating : " + str(num_rating[i*5 + 2]))
			st.text("Avg_rating : " + str(avg_rating[i*5 + 2]))
          	st.text("")
			
		with col4:
          	st.image(url[i*5 + 3])
          	st.text("Name : " + name[i*5 + 3])
          	st.text("Author : " + author[i*5 + 3])
          	st.text("Publisher : " + publisher[i*5 + 3])
          	st.text("Year : " + str(year[i*5 + 3]))
			st.text("Num_rating : " + str(num_rating[i*5 + 3]))
			st.text("Avg_rating : " + str(avg_rating[i*5 + 3]))
          	st.text("")
			
		with col5:
          	st.image(url[i*5 + 4])
          	st.text("Name : " + name[i*5 + 4])
          	st.text("Author : " + author[i*5 + 4])
          	st.text("Publisher : " + publisher[i*5 + 4])
          	st.text("Year : " + str(year[i*5 + 4]))
			st.text("Num_rating : " + str(num_rating[i*5 + 4]))
			st.text("Avg_rating : " + str(avg_rating[i*5 + 4]))
          	st.text("")
     
