import os
import cv2
from os import listdir
from os.path import isfile, join
import argparse
import numpy as np

def convert_yolo_coordinates_to_voc(x_c_n, y_c_n, width_n, height_n, img_width, img_height):
  x_c = float(x_c_n) * img_width
  y_c = float(y_c_n) * img_height
  width = float(width_n) * img_width
  height = float(height_n) * img_height
  half_width = width / 2
  half_height = height / 2
  left = int(x_c - half_width) + 1
  top = int(y_c - half_height) + 1
  right = int(x_c + half_width) + 1
  bottom = int(y_c + half_height) + 1
  return [left, top, right, bottom]

parser = argparse.ArgumentParser(description='Path to dataset')
parser.add_argument('path')
args = parser.parse_args()
path = args.path

resPath = 'res/'
if not os.path.exists(resPath):
    os.makedirs(resPath)

onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
filenames = []

for e in onlyfiles:
    n,_ = e.split('.')
    if n not in filenames:
        filenames.append(n)

for e in filenames:
    imagename = path + str(e) + '.jpg'
    textname= path + str(e) + '.txt'

    img = cv2.imread(imagename)
    height, width, bpp = np.shape(img)

    f = open(textname,'r')
    for l in f:
        a = l.strip().split(' ')
        voc = convert_yolo_coordinates_to_voc(a[1],a[2],a[3],a[4],width,height)
        print(voc)
        cv2.rectangle(img, (int(voc[0]), int(voc[1])), (int(voc[2]), int(voc[3])), (0,0,255), 2)
    cv2.imwrite(resPath + e + ".jpg" ,img)
