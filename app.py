import streamlit as st

st.title("My First Streamlit Project")

st.write("Welcome to my application!")

name = st.text_input("Enter your name")

if st.button("Submit"):
    st.success(f"Welcome {name}!")