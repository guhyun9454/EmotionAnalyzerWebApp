import cv2
import mediapipe as mp
import numpy as np
from keras.models import load_model
from PIL import Image, ImageDraw, ImageFont

model_path = "src/v2_final.hdf5"
model = load_model(model_path)
font_path = "src/NanumGothic.ttf"
emotions_korean = ["분노", "슬픔", "당황", "기쁨", "중립"]
mp_face_detection = mp.solutions.face_detection
face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)

def process_image(image):
    frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    ih, iw, _ = frame.shape
    font_size = int(ih / 12)
    font = ImageFont.truetype(font_path, font_size)

    pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(pil_image)

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_detection.process(rgb_frame)

    if results.detections:
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            x, y, w, h = int(bboxC.xmin * iw), int(bboxC.ymin * ih), int(bboxC.width * iw), int(bboxC.height * ih)

            face = frame[y:y + h, x:x + w]
            face = cv2.resize(face, (48, 48))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) / 255.0
            face = np.expand_dims(face, axis=-1)
            face = np.expand_dims(face, axis=0)

            prediction = model.predict(face)
            text_on_img = emotions_korean[np.argmax(prediction)] + " " + str(round(np.max(prediction), 2))
            draw.text((x, y - font_size), text_on_img, font=font, fill="white")
            draw.rectangle([(x, y), (x + w, y + h)], outline="white", width=font_size // 10)

    return pil_image
