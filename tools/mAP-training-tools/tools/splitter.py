import cv2
import argparse
import os

if not os.path.exists('splits'):
    os.makedirs('splits')

parser = argparse.ArgumentParser(description='Path to video')
parser.add_argument('path')
args = parser.parse_args()

filepath = args.path

with open(filepath) as fp:
   line = fp.readline()
   count = 1
   found = 0

   file = open("splits/"+str(count) + ".txt","w")

   while line:
       line = line.strip()
       tokens = line.split(" ")

       if line == "":
           found += 1

           if found  == 2:
               print(count)
               count += 1
               file = open("splits/"+str(count) + ".txt","w")
               found = 0

       elif len(tokens) == 6 and tokens[0] == "person":
           nline = tokens[0] + " " + tokens[1] + " " + tokens[2] + " " + tokens[3] + " " + tokens[4] + " " + tokens[5]
           print(nline)
           file.write(nline+"\n")
       line = fp.readline()
