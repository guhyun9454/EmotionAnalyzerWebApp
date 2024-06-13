import streamlit as st
import requests
from PIL import Image
from io import BytesIO
import numpy as np

st.title("Emotion Analyzer")
st.write("You can test with a provided test image or upload your own.")

uploaded_file = st.file_uploader("Upload your image...", type=["jpg", "jpeg", "png"])
preloaded_images = {
    "Test Image 1": r"https://blog.hubspot.com/hs-fs/hubfs/Untitled%20design%20%281%29-Aug-02-2022-04-20-22-53-PM.png?width=595&height=400&name=Untitled%20design%20%281%29-Aug-02-2022-04-20-22-53-PM.png"
}
selected_image = st.selectbox("Or choose a preloaded image:", list(preloaded_images.keys()))

col1, col2 = st.columns(2)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
elif selected_image:
    image_path = preloaded_images[selected_image]
    response = requests.get(image_path)
    image = Image.open(BytesIO(response.content))
    # image = Image.open(image_path)
    print("test image selected")

if image:
    with col1:
        st.image(image, caption='Selected Image', use_column_width=True)

    url = 'http://ai-server-service:9454/predict'

    if uploaded_file:
        files = {'image': uploaded_file.getvalue()}
    else:
        buffered = BytesIO()
        image = image.convert('RGB')
        image.save(buffered, format="JPEG")
        files = {'image': buffered.getvalue()}

    response = requests.post(url, files=files)

    if response.status_code == 200:
        processed_image = Image.open(BytesIO(response.content))
        with col2:
            st.image(processed_image, caption='Processed Image', use_column_width=True)
    else:
        st.error("Error with processing image. Server responded with: " + response.text)