import os
from os import listdir
import argparse
from os.path import isfile, join

parser = argparse.ArgumentParser(description='rename files')

parser.add_argument('path')
parser.add_argument('start')

args = parser.parse_args()

mypath = args.path
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

filenames = []
_, ext = onlyfiles[0].split('.')


for e in onlyfiles:
    n,_ = e.split('.')
    if n not in filenames:
        filenames.append(n)


for e in filenames:
    j = int(args.start)
    j = int(e) + j
    name = mypath + str(e)
    newname = mypath + str(j)
    os.rename(name + '.txt', newname + '.txt')
    os.rename(name + '.jpg', newname + '.jpg')
