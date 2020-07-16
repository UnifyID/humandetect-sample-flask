import os
import requests
import json
from flask import Flask, request, jsonify
import numpy as np
import cv2
from tensorflow.keras.applications import MobileNet
from tensorflow.keras.applications.mobilenet import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image

app = Flask(__name__)
model = MobileNet(weights='imagenet')
UPLOAD_FOLDER = './uploads'
HEADERS = {
    'Content-Type': 'application/json',
    'X-API-Key': os.environ['UnifyIDAPIKey'],
}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        file = request.files['file']
        token = request.form['token']

        if not file:
            return "Error: file not found in request"

        if not token:
            return "Error: token not found in request"

        print("token:", token)

        hd_response = requests.post('https://api.unify.id/v1/humandetect/verify', headers=HEADERS, data=json.dumps({"token": token}))

        if hd_response.status_code == 400:
            return "Error: invalid HumanDetect token"

        hd_json = hd_response.json()

        if "valid" not in hd_json or not hd_json["valid"]:
            return "Error: HumanDetect verification failed"

        try:
            print("valid human:", hd_response.json()["valid"])

            filename = os.path.join(UPLOAD_FOLDER, "image.png")
            file.save(filename)

            img = cv2.imread(filename)
            img = cv2.resize(img, (224, 224))
            x = image.img_to_array(img)
            x = np.expand_dims(x, axis=0)
            x = preprocess_input(x)
            preds = decode_predictions(model.predict(x), top=5)[0]

            preds_formatted = ", ".join([
              f"{class_description}: {score*100:.2f}%"
              for (_, class_description, score) in preds
            ])

            print("predictions: ", preds_formatted, "\n")
            return preds_formatted

        except Exception as e:
            print(e)
            return "Error: prediction failed, try again later"

    else:
        return "<h1>HumanDetect Example</h1>"
