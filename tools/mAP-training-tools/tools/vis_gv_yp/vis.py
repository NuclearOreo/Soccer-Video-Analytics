import sys
import numpy
import cv2
import os
from os import walk

images = "images/"
gv = "ground-truth/"
predictions = "predicted/"
output = "res/"

if not os.path.exists("res"):
    os.makedirs("res")

imglist = []
for (dirpath, dirnames, filenames) in walk(images):
    imglist.extend(filenames)
    break

for e in imglist:
    e = e.split('.')

    img = cv2.imread(images + e[0] + ".jpg")
    gvfile = open(gv + e[0] + ".txt", "r")
    yolopred = open(predictions + e[0] + ".txt", "r")

    for line in gvfile:
        line = line.strip().split(' ')
        cv2.rectangle(img, (int(line[1]), int(line[2])), (int(line[3]), int(line[4])), (0,255,0), 2)

    for line in yolopred:
            line = line.strip().split(' ')
            cv2.rectangle(img, (int(line[2]), int(line[3])), (int(line[4]), int(line[5])), (0,0,255), 2)

    cv2.imwrite(output + e[0] + ".jpg" ,img)
