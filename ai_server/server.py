from flask import Flask, request, send_file
from PIL import Image
import io
from model import process_image
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return "image not found", 400

    file = request.files['image']
    image = Image.open(file.stream)

    processed_image = process_image(image)
    img_byte_arr = io.BytesIO()
    processed_image.save(img_byte_arr, format='JPEG')
    img_byte_arr.seek(0)

    return send_file(img_byte_arr, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True,port = "30001")