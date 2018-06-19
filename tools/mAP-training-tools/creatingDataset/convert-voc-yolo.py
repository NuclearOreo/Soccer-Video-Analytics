import argparse
import os
import numpy as np
import cv2
from os import listdir
from os.path import isfile, join

if not os.path.exists('converted'):
    os.makedirs('converted')

parser = argparse.ArgumentParser(description='Convert voc to yolo')
parser.add_argument('path')
args = parser.parse_args()

path = args.path

fpath = 'frames/'
cpath = 'converted/'

onlyfiles = [f for f in listdir(fpath) if isfile(join(fpath, f))]

img = cv2.imread(fpath + onlyfiles[0])
height, width, bbx = np.shape(img)

filenames = []
for e in onlyfiles:
    n,_ = e.split('.')
    if n not in filenames:
        filenames.append(n)

def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)

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


list = os.listdir(path) # dir is your directory path
num = len(list)

for e in filenames:
    file = open(path + e + '.txt', 'r')
    fileout = open(cpath + e + '.txt', 'w')

    for line in file:
        tokens = line.strip().split()
        print(width,height)
        print(tokens)

        xmin = tokens[2]
        xmax = tokens[4]
        ymin = tokens[3]
        ymax = tokens[5]

        b = (float(xmin), float(xmax), float(ymin), float(ymax))
        yolo = convert((width,height), b)
        voc = convert_yolo_coordinates_to_voc(yolo[0], yolo[1], yolo[2], yolo[3], width, height)
        print(yolo)
        print(voc)
        nline = str(0) + " " + str(yolo[0]) + " " + str(yolo[1]) + " " + str(yolo[2]) + " " + str(yolo[3])
        print()
        fileout.write(nline + "\n")

    fileout.close()
