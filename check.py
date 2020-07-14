# from PIL import Image
# import numpy as np
# import matplotlib.pyplot as plt

import cv2
# print(cv2.__version__)

# here 0 is for the default laptop webcam
cap = cv2.VideoCapture(0)

# we are using harcascade algorithm for face detection
classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# we are providing loop to capture each frame : which will work like video
while True:
    # it will help to read the stream
    ret, frame = cap.read()
    if ret:
        # we will get answer in form of list as shown above
        # it may have 1 or more faces so using faces as name
        faces = classifier.detectMultiScale(frame)

        # for every face in faces
        for face in faces:
            # each face have their own x,y,w,h value
            x, y, w, h = face
            # here we are talking about cv2 which works on BGR so choose color according to it
            frame = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)

        cv2.imshow("My Window", frame)

    key = cv2.waitKey(1)

    # ord value is the uni-code
    # on clicking the q it will close the window
    if key == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

