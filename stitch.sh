cd extractFrames
rm -r left
rm -r right
mkdir left
mkdir right
cd ../stitcher
rm -r crops
rm -r output
mkdir crops
mkdir output
rm result.mp4
cd ..

# Assume $1 is left and $2 is right.
cd extractFrames

length=$(ffprobe -i $1 -show_entries format=duration -v quiet -of csv="p=0")
# This finds the length of the video in cmd line arg 1
length=${length%.*}
# Convert length of video to nearest int

fps=$(ffprobe -v error -select_streams v -of default=noprint_wrappers=1:nokey=1 -show_entries stream=r_frame_rate $1)
# This finds the frames / seconds
var1=${fps%/*}
var2=${fps#*/}
fps=$(($var1 / $var2))
# This parses fps and returns an actual value

result=$(($length * $fps))
# This multiplies length by fps to find total frame length

echo "Number of frames " $result

python getFrames.py --left $1 --right $2 
# This command runs the python script to convert videos to images.
cd ../stitcher
make 

for i in $(seq 1 $result);
do
  ./stitching ../extractFrames/left/leftFrame$i.jpg ../extractFrames/right/rightFrame$i.jpg --Output output/stitched$i.jpg;
done
# this executable stitched together the images 
mkdir crops
python cropper.py -ext jpg 
# this script crops the image 

python img2video.py -ext jpg -o result.mp4

cd ../videoStabilize
make

./videostab ../stitcher/result.mp4


