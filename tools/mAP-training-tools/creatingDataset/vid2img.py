import cv2
import argparse
import os

if not os.path.exists('frames'):
    os.makedirs('frames')

parser = argparse.ArgumentParser(description='Path to video')
parser.add_argument('path')
args = parser.parse_args()

vidcap = cv2.VideoCapture(args.path)
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("frames/%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
