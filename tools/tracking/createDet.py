from os import listdir
from os.path import isfile, join
import argparse

parser = argparse.ArgumentParser(description='Path to detections')
parser.add_argument('path')
args = parser.parse_args()

mypath = args.path
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
fileout = open('det.txt', 'w')

onlyNumbers = []
for e in onlyfiles:
    a = e.split('.')
    onlyNumbers.append(int(a[0]))
onlyNumbers.sort()

i = 1
for n in onlyNumbers:
    file = open(mypath + str(n) + '.txt', 'r')
    for line in file:
        id, conf, bb_left, bb_top, bb_width, bb_height = line.strip().split(' ')
        fileout.write(str(i) + ',-1,' + str(bb_left) + ',' + str(bb_top) + ',' + str(bb_width) + ',' + str(bb_height) + ',-1,-1,-1,-1\n')
    i += 1

fileout.close
