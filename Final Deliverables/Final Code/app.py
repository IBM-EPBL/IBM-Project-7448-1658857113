import os

from flask import Flask, render_template, request
from PIL import Image
from werkzeug.utils import secure_filename
import numpy as np
import tensorflow as tf


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('recognise.html')


model = tf.keras.models.load_model("digit_classifier.h5")

@app.route('/predict', methods = ['POST'])
def predict():
    if request.method == 'POST':
        img = Image.open(request.files['file']).convert("L")
        img = img.resize((28,28))
        im2arr = np.array(img)
        im2arr = im2arr.reshape(1,28,28,1)
        y_pred = model.predict(im2arr)
        
        return render_template('predict.html', num = str(y_pred))

if __name__ == '__main__' :
    app.run(host='0.0.0.0', port=8000, debug=True, threaded=True)
