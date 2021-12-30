## this is a program that generates a png file from synthetic data from a deviantart user profile
## and saves it into a directory of your choice as a PNG file of a dataset of multiple png files

print("Welcome to the DeviantArt Art Generator!")

print("What style of what artist do you want to generate?")
import os
import gradio as gr
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import matplotlib.cm as cm
import random
import requests
import json
import time
import sys

from tensorflow.python.util.tf_export import KERAS_API_NAME
print("Select a style:")
print("1. Abstract")
print("Anime")
print('f. Fantasy')
print('Minecraft')
#### if if abstract use tensorflow to use a input data from the data set url from a deviant art and generate a png file
#### if anime use tensorflow to use a input data from the data set url from a deviant art and generate a png file
#### if fantasy use tensorflow to use a input data from the data set url from a deviant art and generate a png file
#### if minecraft use tensorflow to use a input data from the data set url from a deviant art and generate a png file
abstractgeneratormoodgenerator=gr.inputs.Input.tensorflow(tf.keras.models.load_model('abstractgeneratormoodgenerator.h5'))
animegeneratormoodgenerator=gr.inputs.Input.tensorflow(tf.keras.models.load_model('animegeneratormoodgenerator.h5'))
fantasygeneratormoodgenerator=gr.inputs.Input.tensorflow(tf.keras.models.load_model('fantasygeneratormoodgenerator.h5'))
minecraftgeneratormoodgenerator=gr.inputs.Input.tensorflow(tf.keras.models.load_model('minecraftgeneratormoodgenerator.h5'))
print("Use the abstract generator to make stylistic arts of any abstract style")
abstractgeneratormoodgenerator.set_title("Abstract Generator")
animegeneratormoodgenerator.set_title("Anime Generator")
fantasygeneratormoodgenerator.set_title("Fantasy Generator")
minecraftgeneratormoodgenerator.set_title("Minecraft Generator")
print("Use the anime generator to make stylistic arts of any anime style")
print("What user would you like to copy?")
print("Write a generative art style ")
KERAS_API_NAME = 'tensorflow'
print("Select a style:")
## write a png and use tensorflow to generate a image from the gans
tensorflowgeneratormoodgenerator=gr.inputs.Input.tensorflow(tf.keras.models.load_model('tensorflowgeneratormoodgenerator.h5'))
tensorflowgeneratormoodgenerator.set_title("Tensorflow Generator")
print("Use the tensorflow generator to make stylistic arts of any style")
## save it to the picture directory
print("What directory would you like to save the generated art to?")
print("Write a directory name")
print("Select a directory")
directoryname=gr.inputs.Input.text()
directoryname.set_title("Directory Name")
print("What is the name of the generated art?")
print("Write a name")
artimagepngname=gr.inputs.Input.text()
artimagepngname.set_title("Art Image Name")
##setheight
print("What height would you like the generated art to be?")
height=gr.inputs.Input.text()
width=gr.inputs.Input.text()
## use the deviantart api to make new images
print("What user would you like to copy?")
print("Write a deviantart user name")
deviantartuser=gr.inputs.Input.text()
deviantartuser.set_title("DeviantArt User")
print("What is the name of the generated art?")
print("Write a name")
artimagepngname=gr.inputs.Input.text()
artimagepngname.set_title("Art Image Name")
## set height
print("What height would you like the generated art to be?")
height=gr.inputs.Input.text()
width=gr.inputs.Input.text()
## use the deviantart api to make new images
print("What user would you like to copy?")
print("Write a deviantart user name")
deviantartuser=gr.inputs.Input.text()
deviantartuser.set_title("DeviantArt User")             
## output folder for the image
print("What directory would you like to save the generated art to?")
outputfolder=gr.inputs.Input.text()
print(deviantartuser)
print(outputfolder)
print(artimagepngname)
print(height)
print(width)
## get the deviantart user data
print('Done.')