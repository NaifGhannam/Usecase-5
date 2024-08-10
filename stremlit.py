import streamlit as st

# Set the app title
st.set_page_config(page_title="My Streamlit App")

# Add a title
st.title("Welcome to My Streamlit App")

# Add an image
image = "range.png"
st.image(image, caption=" range image ")

# Add a statement
statement = "This is a statement about my Streamlit app."
st.write(statement)