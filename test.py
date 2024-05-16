# Import libraries
from tensorflow.keras.applications.vgg16 import VGG16
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.vgg16 import preprocess_input as preprocess_input_vgg16
import numpy as np
import tensorflow.keras as keras
import tensorflow as tf
from matplotlib import pyplot as plt
import gc
from tensorflow.keras.models import Model
from sklearn import decomposition
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
# from mlxtend.plotting import plot_confusion_matrix
from sklearn.metrics import confusion_matrix

import pandas as pd
from PIL import Image
import os
import cv2
from sklearn.model_selection import train_test_split
from tensorflow.keras import models
from tensorflow.keras import layers
from keras.optimizers import Adam
from keras.optimizers import Lion
from keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications.vgg19 import VGG19
from tensorflow.keras.applications.vgg19 import preprocess_input as preprocess_input_vgg19
from tensorflow.keras.models import Sequential, save_model, load_model

test_datagen = ImageDataGenerator(
    # rescale=1./255,
    # preprocessing_function=keras.applications.resnet_v2.preprocess_input,#written over the input data?
    featurewise_center=False)

test_set = test_datagen.flow_from_directory( 'HlZero/thesis/test',
                                            target_size=(224,224),
                                            color_mode="rgb",#??
                                            # classes=['bend', 'fall', 'liedown', 'run', 'sitdown', 'walk'],
                                            classes=['down','fall','move'],
                                            # class_mode="categorical",
                                            class_mode=None,
                                            # batch_size=32,
                                            batch_size=1,
                                            shuffle=False,
                                            seed=None,
                                            save_to_dir=None,
                                            save_prefix="",
                                            save_format="jpg",
                                            follow_links=False,
                                            subset=None,
                                            interpolation="nearest",
                                         )
model = load_model('HlZero/thesis/model_weights.h5', compile = True)

predictions = model.predict(test_set)
print(predictions)

# Generate arg maxes for predictions
classes = np.argmax(predictions, axis = 1)
print(classes)