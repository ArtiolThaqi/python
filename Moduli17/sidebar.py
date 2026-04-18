import streamlit as st

st.sidebar.header("Sidebar")

st.sidebar.write("This is a sidebar")

st.sidebar.selectbox("Select an option",["Option 1","Option 2","Option 3","Option 4"])

st.sidebar.radio("Go to",["Home","Data","Settings"])