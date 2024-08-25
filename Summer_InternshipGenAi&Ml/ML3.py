from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.preprocessing import image

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    file = request.files['file']
    img = image.load_img(file, target_size=(64, 64))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)

    return jsonify({'predicted_class': int(predicted_class[0])})

if __name__ == '__main__':
    app.run(debug=True)
