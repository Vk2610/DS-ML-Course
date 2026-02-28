import streamlit as st

# Title of the app
st.title("Streamlit Widgets Example")

# Create a text input widget
name = st.text_input("Enter your name:")
# Create a slider widget
age = st.slider("Select your age:", 0, 100, 25) 
# Create a selectbox widget 
city = st.selectbox("Select your city:", ["New York", "Los Angeles", "Chicago", "Houston"])
# Display the input values

st.write(f"Hello {name}, you are {age} years old and live in {city}.")
