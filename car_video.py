import cv2
from random import randrange

# Load the pre-trained data
car_tracker = cv2.CascadeClassifier(r'C:\Users\udaya\OneDrive\Documents\cars.xml')

# read the given video
car_video = cv2.VideoCapture(r'C:\Users\udaya\Downloads\Cars_video.mp4')

#Iterating forever over frames
while True:
    #read the current frame
    frame_check,frame=car_video.read()
    
    #converting to B&W
    gr_img= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    
    # detecting the coordinates of the car
    car_coordinates = car_tracker.detectMultiScale(gr_img)
    
    #marking the cars
    for (x,y,w,h) in car_coordinates:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(randrange(256),randrange(256),randrange(256)),2)
    
    #display the current frame
    cv2.imshow('cars',frame)
    key = cv2.waitKey(1)
    
    #stopping condition
    if key == 83 or key== 115:
        break

# release the VideoCapture object
car_video.release()
    

print('Press "s" to stop')

print('Hey!')
