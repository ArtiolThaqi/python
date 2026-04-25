import streamlit as st

if st.button("Click Me"):
    st.write("Button Clicked")


if st.checkbox("Check me to show some text"):
    st.write("You'ree seeing this text because you checked the checkbox")


user_input = st.text_input("Enter text","Simple text")
st.write("You entered:", user_input)

age = st.number_input("Enter your age",min_value=0, max_value=100)
st.write("Your age is:",age)

message = st.text_area("Enter a message")
st.write("Your message:", message)


choice = st.radio("Pick one",["HTML","CSS","Python"])
st.write("Your choice is:" ,choice)

if st.button("Success"):
    st.success("Operation was successful")


try:
    1/0
except Exception as e:
    st.exception(e)