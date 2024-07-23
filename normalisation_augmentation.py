import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator

# define ImageDataGenerator with normalization and augmentation for training
train_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest',
    validation_split=0.2  # 20% of the data for validation
)

# define ImageDataGenerator for validation with normalization only
validation_datagen = ImageDataGenerator(
    rescale=1.0/255.0,
    validation_split=0.2  # 20% of the data for validation
)

# create training generator
train_generator = train_datagen.flow_from_directory(
    'D:\\diabetic-retinopathy-detection\\train\\train',
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='training'  # use the training subset
)

# create validation generator
validation_generator = validation_datagen.flow_from_directory(
    'D:\\diabetic-retinopathy-detection\\train\\train',  # same directory as training
    target_size=(224, 224),
    batch_size=32,
    class_mode='binary',
    subset='validation'  # use the validation subset
)

__all__ = ['train_generator', 'validation_generator']
