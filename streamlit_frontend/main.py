import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import numpy as np

st.title('이미지 처리 서버')
st.write('업로드할 이미지를 선택해 주세요.')

uploaded_file = st.file_uploader("사진을 선택해 주세요...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Processing...")

    url = 'http://ai_server:9454/predict'

    files = {'image': uploaded_file.getvalue()}
    response = requests.post(url, files=files)

    if response.status_code == 200:
        processed_image = Image.open(BytesIO(response.content))
        st.image(processed_image, caption='Processed Image', use_column_width=True)
    else:
        st.error("Error with processing image. Server responded with: " + response.text)
