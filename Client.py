## this is a art GAN using stylegan ada 3 and tensorflow gpu model to produce art in the style
## of ddlc and monika after story renpy

import argparse
import os
import sys
import random
import numpy as np
### activate conda environment
conda_env = os.environ["CONDA_DEFAULT_ENV"]
activate_this = os.path.join(os.environ["CONDA_PREFIX"], "etc/profile.d/conda.sh")
exec(open(activate_this).read(), dict(__file__=activate_this))
## use conda for machine learning with t5 gpu google
conda_env = os.environ["CONDA_DEFAULT_ENV"]
t5 = os.path.join(os.environ["CONDA_PREFIX"], "etc/profile.d/t5.sh")
## download google t5 model from github
print("Syncing model with t5 model from github")
os.system("pip install t5")
print("Done")
##
print("Ask the user how many images they want to create")
num_images = int(input("How many images do you want to create? "))
print("Ask the user what style they want to use")
style = input("What style do you want to use? ")
print("Ask the user what size they want to use")
size = int(input("What size do you want to use? "))
print("Ask the user what resolution they want to use")
resolution = int(input("What resolution do you want to use? "))
## ask the user what base image to use
baseimage=input("What base image do you want to use? ")
## use the t5 model to generate a new image of the style that the user wants in anaconda
## activate tensorflow in anaconda
print("Activating tensorflow in anaconda")
os.system.conda_env("activate", "tensorflow")
## write the desired style to the new output

## use the gpu to train on a folder of images and
## and then output a sprite pack for the games style that you want using a folder of num_images
imagefoldertemplate=input("What folder do you want to use? ")
## combine the base image and then generate a file in your selected folder calledo output.png
## and then use the sprite packer to generate a sprite pack
# done
outputimage=os.path.join(os.getcwd(), "output.jpg")

print("GAN Done. Exit now. Thanks.s")