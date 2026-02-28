import streamlit as st
import pandas as pd
import numpy as np

# Title of the app

st.title("My First Streamlit App")


# Display a simple text

st.write("Hello, welcome to my Streamlit app!")

# create and display a dataframe

data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [25, 30, 35, 40],
    "City": ["New York", "Los Angeles", "Chicago", "Houston"]
}

df = pd.DataFrame(data)

st.dataframe(df)
# Create and display a line chart
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["A", "B", "C"]
)

st.line_chart(chart_data)