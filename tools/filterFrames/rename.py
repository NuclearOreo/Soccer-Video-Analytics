import os
from os import listdir
from os.path import isfile, join

mypath = "filtered/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

nums = []
_, ext = onlyfiles[0].split('.')


for e in onlyfiles:
    num,_ = e.split('.')
    nums.append(int(num))

nums.sort()

for i in range(len(nums)):
    name = mypath + str(nums[i]) + "." + ext
    newname = mypath + str(i) + "." + ext
    os.rename(name, newname)
