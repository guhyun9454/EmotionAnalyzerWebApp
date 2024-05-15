import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import numpy as np

st.title("Emotion Analyzer")
st.write("You can test with test image provided")

uploaded_file = st.file_uploader("Select image...", type=["jpg", "jpeg", "png"])
col1, col2 = st.columns(2)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    with col1:
        st.image(image, caption='Uploaded Image', use_column_width=True)

    url = 'http://ai_server:9454/predict'

    files = {'image': uploaded_file.getvalue()}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        processed_image = Image.open(BytesIO(response.content))
        with col2:
            st.image(processed_image, caption='Processed Image', use_column_width=True)
    else:
        st.error("Error with processing image. Server responded with: " + response.text)
