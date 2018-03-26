import cv2
import imutils
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-l", "--left", required=True, default='left.mp4', help="extension name. default is 'png'.")
ap.add_argument("-r", "--right", required=True, default='right.mp4', help="output video file")
args = vars(ap.parse_args())

vidcap = cv2.VideoCapture(args['left'])
vidcap2 = cv2.VideoCapture(args['right'])
success,image = vidcap.read()
success2,image2 = vidcap2.read()
count = 0
success = True

while success:
  #image = imutils.rotate(image, angle=180)
  cv2.imwrite("left/leftFrame%d.jpg" % count, image)     # save frame as JPEG file
  cv2.imwrite("right/rightFrame%d.jpg" % count, image2)     # save frame as JPEG file

  success,image = vidcap.read()
  succes2,image2 = vidcap2.read()
  print('Read a new frame: ', success, count)
  print('Read a new frame: ', success2, count)
  count += 1
