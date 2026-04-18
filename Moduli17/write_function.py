import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Name': ["Alice", "Bob", "Carol"],
    'Age': [20, 30, 40],
    'City': ['New York', 'San Diego', 'San Francisco'],
})


st.write(df)