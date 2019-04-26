# import the neccessary packages
from keras.applications import ResNet50
from keras.preprocessing.image import img_to_array
from keras.applications import imagenet_utils
from PIL import Image
import numpy as np
import flask
import io

# initialize flask app and model
app = flask.Flask(__name__)
model = None





