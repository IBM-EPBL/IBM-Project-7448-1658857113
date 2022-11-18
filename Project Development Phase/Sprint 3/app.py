import numpy as np
import os
# import tensorflow
from PIL import Image
from flask import Flask, request, render_template, url_for
from werkzeug.utils import secure_filename, redirect
from gevent.pywsgi import WSGIServer
from keras.models import load_model
from keras.preprocessing import image
from flask import send_from_directory
# import tensorflow.compat.v2 as tf

FOLDER =r'C:\Users\Janeswaran\OneDrive\Desktop\img'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = FOLDER

model = load_model("digit_classifier.h5")

@app.route('/')
def index():
    return render_template('recognise.html')

@app.route('/predict', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        f = request.files["image"]
        filepath = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filepath))
        uploading_img = os.path.join(FOLDER, filepath)
        img = Image.open(uploading_img).convert("L") 
        img = img.resize((28, 28))
        im2arr = np.array(img)
        im2arr = im2arr.reshape(1, 28, 28, 1)
        predict = model.predict(im2arr)
        num = np.argmax(predict, axis=1)
        return render_template('predict.html', num=str(num[0]))

if __name__ == '__main__':
    app.run(debug=True, threaded=False)
