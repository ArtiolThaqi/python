import streamlit as st
import pandas as pd
import plotly.express as px

from Moduli18.data_visualization import unique_titles, average_rating

books_df=pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling Books Analysis ")
st.write("This app analyzes the Amazon top selling books")

st.subheader("Amazon top selling books")
total_books=books_df.shape[0]

unique_titles=books_df['Name'].nunique()
average_rating=books_df['Rating'].mean()
average_price=books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", f"{average_rating:.2f}")
col2.metric("Average Price", f"{average_price:.2f}")

st.subheader("Dataset preview")
st.write(books_df.head(10))

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Books Titles")
    top_titles=books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

with col2:
    st.subheader("Top 10 Authors")
    top_authors=books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

st.subheader("Genre Distribution")
fig=px.pie(books_df,names='Genre',title='Most Liked Genre',color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig)

st.subheader("Number of fiction vs Non fiction books over the years")
size=books_df.groupby(['Year','Genre']).size().reset_index('Counts')
fig1=px.bar(size,x='Year',y='Counts',color='Genre',title='Number of Books Over Years',
           color_discrete_sequence=px.colors.sequential.Plasma,barmode='group')
st.plotly_chart(fig1)

st.subheader("Top 15 Authors by Counts of Books Published")
top_authors=books_df['Author'].value_counts().head(15).reset_index("Count")
fig2=px.bar(top_authors,x='Author',y='Count',orientation='h',title='Top 15 Authors by Counts',
           labels={"Author":"Name of author","Count":"Number of books published"},
           color="Count",color_discrete_sequence=px.colors.sequential.Plasma)
st.plotly_chart(fig2)

st.subheader("Filter data by Genre")
genre_filter=st.selectbox("Select Genre",books_df['Genre'].unique())
filtered_data=books_df[books_df['Genre']==genre_filter]
st.write(filtered_data)




