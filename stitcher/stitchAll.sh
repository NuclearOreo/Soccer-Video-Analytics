for i in {0..596};
do
  ./stitching ../extractFrames/left/leftFrame$i.jpg ../extractFrames/right/rightFrame$i.jpg --Output output/stitched$i.jpg --d3;
done
