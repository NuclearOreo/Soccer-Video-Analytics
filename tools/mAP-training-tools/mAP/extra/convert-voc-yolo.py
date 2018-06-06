import argparse
import os

if not os.path.exists('converted'):
    os.makedirs('converted')

parser = argparse.ArgumentParser(description='Convert voc to yolo')

parser.add_argument('path')
parser.add_argument('width')
parser.add_argument('height')

args = parser.parse_args()

path = args.path
height = float(args.height)
width = float(args.width)

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

list = os.listdir(path) # dir is your directory path
num = len(list)

for i in range(0,num):
    file = open(path + str(i) + '.txt', 'r')
    fileout = open("converted/" + str(i) + '.txt', 'w')

    for line in file:
        tokens = line.strip().split()

        xmin = tokens[1]
        xmax = tokens[3]
        ymin = tokens[2]
        ymax = tokens[4]

        b = (float(xmin), float(xmax), float(ymin), float(ymax))
        yolo = convert((width,height), b)
        nline = str(0) + " " + str(yolo[0]) + " " + str(yolo[1]) + " " + str(yolo[2]) + " " + str(yolo[3])
        fileout.write(nline + "\n")

    fileout.close()
