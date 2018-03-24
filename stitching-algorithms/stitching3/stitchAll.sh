for i in {0..1026};
do
  ./stitching leftFrames/leftFrame$i.jpg rightFrames/rightFrame$i.jpg --Output stitched$i.jpg;
done
