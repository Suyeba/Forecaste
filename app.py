import streamlit as st
import pickle
import numpy as np

model = pickle.load(open('forecast_model.pkl', 'rb'))

# Define the HTML content with color styling for the title
title_html = """
    <div style="background-color: #025246; padding: 10px;">
        <h1 style="color: white; text-align: center;">Terror Attack Prediction</h1>
    </div>
"""

# Render the title using st.markdown() with unsafe_allow_html=True
st.markdown(title_html, unsafe_allow_html=True)

# Streamlit app title and introduction
st.write("This app forecasts the crude oil price")






