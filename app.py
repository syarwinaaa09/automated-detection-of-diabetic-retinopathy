from flask import Flask, request, render_template, redirect, url_for
import os
from werkzeug.utils import secure_filename
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

app = Flask(__name__)

# configure upload folder
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# load the trained model
model = tf.keras.models.load_model("E:\\diabetic-retinopathy-detection\\trained_model.h5")

# define a function to prepare the image
def prepare_image(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # normalize to [0,1] range
    return img_array

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            img_array = prepare_image(file_path)
            prediction = model.predict(img_array)
            pred_class = 'Diabetic Retinopathy' if prediction[0][0] > 0.5 else 'No Diabetic Retinopathy'
            return render_template('result.html', prediction=pred_class, filename=filename)
    return render_template('upload.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return redirect(url_for('static', filename='uploads/' + filename))

if __name__ == '__main__':
    app.run(debug=True)