import cv2
vidcap = cv2.VideoCapture('ussi2.mp4')
success,image = vidcap.read()
count = 0
success = True
while success:
  cv2.imwrite("frames/%d.jpg" % count, image)     # save frame as JPEG file
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
