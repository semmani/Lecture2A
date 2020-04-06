import cv2, time
import numpy as np
video = cv2.VideoCapture(0)
framecount = 0

while True:

    check , frame = video.read()
    framecount += 1

    print("----frame--------")
    print(frame)
    cv2.imshow("'myvideo",frame)
    #cv2.imshow("rotated img-->",np.rot90(frame)) # we are rotating the frames and then videoing it
    key = cv2.waitKey(1)  # 1 is 1 milli-second
    if key == ord('q'):
        break
print("Total Frames are: ", framecount) # to write how many frames are captured
video.release()
cv2.destroyAllWindows()

#for reference to OpenCv--> docs.opencv.org---> EXPLORE IT!!

#Assignment -> use opencv and its api to save the list of frames so that it later runs like a video file.


