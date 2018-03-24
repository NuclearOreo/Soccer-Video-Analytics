#!/usr/local/bin/python3

import cv2
import argparse
import os

# Construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-ext", "--extension", required=False, default='png', help="extension name. default is 'png'.")
args = vars(ap.parse_args())

# Arguments
dir_path = 'results'
ext = args['extension']

images = []
for f in os.listdir(dir_path):
    if f.endswith(ext):
        images.append(f)

# Determine the width and height from the first image
image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape


images = sorted(images)

for image in images:

    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)

    crop_img = frame[500:1750, 80:6000]

    cv2.imshow('video',crop_img)
    if (cv2.waitKey(1) & 0xFF) == ord('q'): # Hit `q` to exit
        break

# Release everything if job is finished
cv2.destroyAllWindows()