import sys

def convert_yolo_coordinates_to_voc(x_c_n, y_c_n, width_n, height_n, img_width, img_height):
  ## remove normalization given the size of the image
  x_c = float(x_c_n) * img_width
  y_c = float(y_c_n) * img_height
  width = float(width_n) * img_width
  height = float(height_n) * img_height
  ## compute half width and half height
  half_width = width / 2
  half_height = height / 2
  ## compute left, top, right, bottom
  ## in the official VOC challenge the top-left pixel in the image has coordinates (1;1)
  left = int(x_c - half_width) + 1
  top = int(y_c - half_height) + 1
  right = int(x_c + half_width) + 1
  bottom = int(y_c + half_height) + 1
  return [left, top, right, bottom]


for i in range(0,41):

    name = str(i) + ".txt"
    file = open(name, "r")
    fileout = open("../converted/" + name, "w")

    for line in file:
        line = line.strip().split(" ")
        convert = convert_yolo_coordinates_to_voc(line[2],line[3],line[4],line[5],1920,310)

        if line[0] == "0":
            fileout.write("person " + line[1] + " " + str(convert[0]) + " " + str(convert[1]) + " " + str(convert[2]) + " " + str(convert[3]) + "\n")
