import streamlit as st
import pandas as pd
import numpy as np

# Title for the app
st.title("Welcome to My First Streamlit App 🎉")

# Subtitle or description
st.write("This is a simple Streamlit app to demonstrate some basic features.")

# Text input for user name
name = st.text_input("Enter your name:", "Guest")
if name:
    st.write(f"Hello, {name}! 👋")

# Slider input
age = st.slider("Select your age:", 1, 100, 25)
st.write(f"You are {age} years old.")

# Generate random data for a chart
st.write("Here's a random line chart based on your age:")
chart_data = pd.DataFrame(
    np.random.randn(20, 3) * age,  # Scale the data by age
    columns=["A", "B", "C"]
)
st.line_chart(chart_data)

# Checkbox to toggle a message
if st.checkbox("Click to show a surprise message"):
    st.write("🎉 You found the hidden surprise!")

# Dropdown menu
option = st.selectbox(
    "Which programming language do you like?",
    ["Python", "JavaScript", "C++", "Java"]
)
st.write(f"You selected: {option}")
