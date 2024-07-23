import os
from PIL import Image

def verify_images(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
            try:
                img = Image.open(os.path.join(directory, filename))
                img.verify()  # verify that it is an image
            except (IOError, SyntaxError) as e:
                print(f'Bad file: {filename}')

verify_images('D:\\diabetic-retinopathy-detection\\train\\train')