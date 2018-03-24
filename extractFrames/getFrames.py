import cv2
import imutils

print(cv2.__version__)

vidcap = cv2.VideoCapture('right.mp4')
success,image = vidcap.read()
count = 0
success = True

while success:
  #image = imutils.rotate(image, angle=180)
  cv2.imwrite("rightFrame%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success, count)
  count += 1
