import tensorflow as tf
from tensorflow import keras
import pandas as pd
import numpy as np
import matplotlib as plt
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Model


print(tf.__version__)

TRAIN_DIR = 'C:/Users/chathurangan.EMBLA/Desktop/New folder/Natural/natural_dataset'

class_names = ['airplane', 'car', 'cat', 'dog', 'flower', 'fruit', 'motorbike', 'person']

train_datagen = ImageDataGenerator(rescale=1. / 255,
                                   shear_range=0.2,
                                   zoom_range=0.2,
                                   horizontal_flip=True,
                                   )
train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(28, 28),
    batch_size=20,
    class_mode='binary',
    subset='training'
)
validation_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=(28,28),
    batch_size=15,
    class_mode='binary',
    subset='validation'

)
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10, activation='softmax')
])
model.fit_generator(
    train_generator,
    steps_per_epoch = train_generator.samples,
    validation_data = validation_generator,
    validation_steps = validation_generator.samples,
    epochs = 5)
