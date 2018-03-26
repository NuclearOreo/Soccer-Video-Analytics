# Soccer-Video-Analytics

README.MD

This compilation of open source frameworks are used to
    
    - Convert video files to images
    - Stitch those images together
    - Crop the footage to a specified size
    - Convert those stitched images to a video
    - Stabilize the video.

To begin, place your videos in the extractedVideos folder.

Then cd into the main directory and call 

./stitch.sh leftvideo.mp4 rightvideo.mp4

where leftvideo.mp4 and rightvideo.mp4 are the videos you add to the extractVideos folder.

command line arguments

    Specifies the right video to be stithed. Required.
    --gpu -g yes/no
    TODO: Adds gpu ability. Not Required.
    
TODO: To find the proper dimensions for cropping, we must 
    - stitch one image together
    - allow the user to pick the corners of the field
    - set those as the stitched parameters
    - pass those parameters to the script
    - crop stitched images to that size

