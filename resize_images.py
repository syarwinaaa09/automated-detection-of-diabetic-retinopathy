import os
from PIL import Image

def resize_images(directory, target_size):
    for filename in os.listdir(directory):
        if filename.endswith('.jpeg') or filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(directory, filename)
            img = Image.open(img_path)
            img = img.resize(target_size)
            img.save(img_path)

resize_images('D:\\diabetic-retinopathy-detection\\train\\train', (224, 224))
resize_images('D:\\diabetic-retinopathy-detection\\test\\test', (224, 224))