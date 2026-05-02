import pandas as pd
import streamlit as st
import plotly.express as px

# Load dataset
book_df = pd.read_csv('bestsellers_with_categories_2022_03_27.csv')

st.title("Bestselling Book Analysis")
st.write("This app analyzes the Amazon top selling books from 2009 to 2022")

# =========================
# ADD NEW BOOK (SIDEBAR)
# =========================
st.sidebar.header('Add New Book Data')

with st.sidebar.form('book_form'):
    new_name = st.text_input('Book Name')
    new_author = st.text_input('Author Name')
    new_user_rating = st.slider('User Rating', 0.0, 5.0, 0.0, 0.1)
    new_reviews = st.number_input('Reviews', min_value=0, step=1)
    new_price = st.number_input('Price', min_value=0, step=1)
    new_year = st.number_input('Year', min_value=2009, max_value=2022, step=1)
    new_genre = st.selectbox('Genre', book_df['Genre'].unique())
    submit_button = st.form_submit_button(label='Add New Book')

if submit_button:
    new_data = {
        'Name': new_name,
        'Author': new_author,
        'User Rating': new_user_rating,
        'Reviews': new_reviews,
        'Price': new_price,
        'Year': new_year,
        'Genre': new_genre
    }

    book_df = pd.concat([pd.DataFrame(new_data, index=[0]), book_df], ignore_index=True)
    book_df.to_csv('bestsellers_with_categories_2022_03_27.csv', index=False)
    st.sidebar.success('New Book Added!')

# =========================
# FILTERS
# =========================
st.sidebar.header('Filter Options')

selected_author = st.sidebar.selectbox("Select Author", ["All"] + list(book_df['Author'].unique()))
selected_year = st.sidebar.selectbox("Select Year", ["All"] + list(book_df['Year'].unique()))
selected_genre = st.sidebar.selectbox("Select Genre", ["All"] + list(book_df['Genre'].unique()))

min_rating = st.sidebar.slider('Minimum User Rating', 0.0, 5.0, 0.0, 0.1)
max_price = st.sidebar.slider('Maximum Price', 0, int(book_df['Price'].max()), int(book_df['Price'].max()))

filtered_books_df = book_df.copy()

# Apply filters
if selected_author != 'All':
    filtered_books_df = filtered_books_df[filtered_books_df['Author'] == selected_author]

if selected_year != 'All':
    filtered_books_df = filtered_books_df[filtered_books_df['Year'] == selected_year]

if selected_genre != 'All':
    filtered_books_df = filtered_books_df[filtered_books_df['Genre'] == selected_genre]

# IMPORTANT FIX (kllapat)
filtered_books_df = filtered_books_df[
    (filtered_books_df['User Rating'] >= min_rating) &
    (filtered_books_df['Price'] <= max_price)
]

# =========================
# SUMMARY
# =========================
st.subheader('Summary Statistics')

total_books = filtered_books_df.shape[0]
unique_titles = filtered_books_df['Name'].nunique()
average_rating = filtered_books_df['User Rating'].mean()
average_price = filtered_books_df['Price'].mean()

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating", round(average_rating, 2))
col4.metric("Average Price", round(average_price, 2))

# =========================
# DATA PREVIEW
# =========================
st.subheader('Filtered Dataset')
st.write(filtered_books_df.head())

# =========================
# CHARTS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.subheader('Top 10 Authors')
    top_authors = filtered_books_df['Author'].value_counts().head(10)
    st.bar_chart(top_authors)

with col2:
    st.subheader('Top 10 Book Titles')
    top_titles = filtered_books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)

# =========================
# PIE CHART (PRO VERSION)
# =========================
st.subheader('Genre Distribution')

genre_counts = filtered_books_df['Genre'].value_counts().reset_index()
genre_counts.columns = ['Genre', 'Count']

fig = px.pie(
    genre_counts,
    names='Genre',          # FIX
    values='Count',         # PRO
    title='Most Liked Genre (2009-2022)',
    color='Genre',
    color_discrete_sequence=px.colors.sequential.Plasma
)

st.plotly_chart(fig)

#Number of fictions and Nonfictions books over the year

st.header('Number of Fiction and Non-fiction books over the year')
size = filtered_books_df.groupby(['Year','Genre']).size().reset_index(name='Counts')
fig = px.bar(size, x='Year',y='Counts',color='Genre',title='Number of Fiction and Non-fiction books over the year',
             color_discrete_sequence=px.colors.sequential.Plasma,barmode='group')
st.plotly_chart(fig)