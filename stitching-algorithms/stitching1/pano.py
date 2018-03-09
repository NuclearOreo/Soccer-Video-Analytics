# import the necessary packages
from stitcher import Stitcher
import argparse
import imutils
import cv2

# construct the argument parse and parse the arguments
#ap = argparse.ArgumentParser()
#ap.add_argument("-f", "--first", required=True,
	#help="path to the first image")
#ap.add_argument("-s", "--second", required=True,
	#help="path to the second image")
#args = vars(ap.parse_args())

# load the two images and resize them to have a width of 400 pixels
# (for faster processing)
#imageA = cv2.imread(args["first"])
#imageB = cv2.imread(args["second"])
#imageA = imutils.resize(imageA, width=900)
#imageB = imutils.resize(imageB, width=900)

# stitch the images together to create a panorama
#stitcher = Stitcher()
#result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)

# show the images
#cv2.imshow("Image A", imageA)
#cv2.imshow("Image B", imageB)
#cv2.imshow("Keypoint Matches", vis)
#cv2.imshow("Result", result)
#cv2.waitKey(0)

	#Path to the videos
vPath1 = "../../../left.mp4"
vPath2 = "../../../right.mp4"

#Path to the Images
iPath1 = ""
iPath2 = ""

#Capture of videos
cap1 = cv2.VideoCapture(vPath1)
cap2 = cv2.VideoCapture(vPath2)

while True:
	ret1, frame1 = cap1.read()
	ret1, frame2 = cap2.read()

	frame1 = imutils.resize(frame1, width=900)
	frame1 = imutils.rotate(frame1, 180)
	frame2 = imutils.resize(frame2, width=900)

	cv2.imshow('frame1', frame1)
	cv2.imshow('frame2', frame2)

	stitcher = Stitcher()
	result, vis = stitcher.stitch([frame1, frame2], showMatches=True)

	cv2.imshow("Result", result)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
