import streamlit as st
import pandas as pd
import plotly.express as px

book_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title('Bestselling Books Analysis')
st.write('This app analyzes the Amazon Top Selling Books from 2009 to 2022.')

st.subheader('Summary Statistics')

total_books = book_df.shape[0]
unique_titles = book_df['Name'].nunique()
average_rating = book_df['User Rating'].mean() #mean llogarit mesataren
average_price = book_df['Price'].mean()

#shfaqja elementeve ne kolona
col1,col2,col3,col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", average_rating)
col4.metric("Average Price", average_price)

st.subheader('Dataset Preview')
st.write(book_df.head())

col1,col2 = st.columns(2)

with col1:
    st.subheader('Top 10 Book Titles')
    top_titles = book_df['Author'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader('Top 10 Authors')
    top_authors = book_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)


#Top 15 authors by Counts of Books Published

st.subheader("Top 15 Authors by Counts of Books Published(2009-2022)")
top_authors = book_df['Author'].value_counts().head(15).reset_index()
top_authors.columns = ['Author','Count']
fig = px.bar(top_authors, x='Count', y='Author',orientation='h',
             title='Top 15 Authors by Counts of Books Published',
             labels={'Count':'Counts of Books Published', 'Author':'Author'},
             color = 'Count', color_continuous_scale=px.colors.sequential.Plasma)

st.plotly_chart(fig)