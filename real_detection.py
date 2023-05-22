import cv2 as cv
import numpy as np
import tensorflow as tf

# getting the video from laptop camera 
# later change to external video camera
cap = cv.VideoCapture(0)

while(True):
    # capture video frame by frame
    ret, frame = cap.read()

    # resizes frame size to 450x450
    resized_frame = cv.resize(frame, (450, 450))

    rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
    resized = tf.image.resize(rgb, (150,150))

    yhat = model.predict(np.expand_dims(resized/255,0))
    sample_coords = yhat[1][0]
    
    # style
    if yhat[0] > 0.5: 
        # Controls the main rectangle
        cv.rectangle(frame, 
                      tuple(np.multiply(sample_coords[:2], [450,450]).astype(int)),
                      tuple(np.multiply(sample_coords[2:], [450,450]).astype(int)), 
                            (255,0,0), 2)
        # Controls the label rectangle
        cv.rectangle(frame, 
                      tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int), 
                                    [0,-30])),
                      tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                    [80,0])), 
                            (255,0,0), -1)
        
        # Controls the text rendered
        cv.putText(frame, 'face', tuple(np.add(np.multiply(sample_coords[:2], [450,450]).astype(int),
                                               [0,-5])),
                    cv.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2, cv.LINE_AA)
    
    cv.imshow('EyeTrack', frame)

    # break out of the loop
    if cv.waitKey(20) & 0xFF == ord('q'):
        break

# when done with use - release video
cap.release()
cv.destroyAllWindows()
