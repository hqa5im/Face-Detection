import cv2 as cv
import os
import time
import uuid

# setup
uuid.uuid1()
IMAGES_PATH = os.path.join('data', 'pictures')
num_images = 20

# to get pictures for our dataset
cap = cv.VideoCapture(0)

# takes images at 0.5 intervals
for num in range(num_images):
    # capture video frame by frame
    ret, frame = cap.read()

    img_name = os.path.join(IMAGES_PATH,f'{str(uuid.uuid1())}.jpg')
    cv.imwrite(img_name, frame)

    # display resulting frame
    cv.imshow('frame', frame)
    time.sleep(0.5)

    # break out of the loop
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# when done with use - release video
cap.release()
cv.destroyAllWindows()