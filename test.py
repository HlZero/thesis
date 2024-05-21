# Import libraries
import numpy as np


import tensorflow as tf
#keras = tf.keras
#models = tf.keras.models
#load_model = tf.keras.models.load_model


#from keras.preprocessing import image
#from keras.applications.vgg16 import preprocess_input as preprocess_input_vgg16
#from keras.preprocessing.image import ImageDataGenerator
#from keras.models import load_model

from sklearn import decomposition
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import train_test_split

test_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    # rescale=1./255,
    # preprocessing_function=keras.applications.resnet_v2.preprocess_input,#written over the input data?
    featurewise_center=False)

test_set = test_datagen.flow_from_directory('test',
                                            target_size=(224,224),
                                            color_mode="rgb",#??
                                            # classes=['bend', 'fall', 'liedown', 'run', 'sitdown', 'walk'],
                                            classes=['down','fall','move'],
                                            class_mode="categorical",
                                            #class_mode=None,
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
model = tf.keras.models.load_model('model_weights.h5', compile = True)

#model.summary()
#print(model.layers[0])
predictions = model.predict(test_set)
print(predictions)

# Generate arg maxes for predictions
pred_classes = np.argmax(predictions, axis = 1)
print(pred_classes)

#Evaluate model
score=model.evaluate(test_set, verbose=1)
print(f'test loss:{score[0]}, test accuracy:{score[1]}')
#true_classes=test_set.classes
#acc=accuracy_score(true_classes,pred_classes)
#print(acc)
#print(true_classes)

