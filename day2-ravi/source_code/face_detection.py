import numpy as np
import cv2
# reading cascade file
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
#web cam opening
cap = cv2.VideoCapture(0)
x=1
while 1:
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # detect objects using cascade files
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #drawing rectangle with blue color and with thickness around face
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    cv2.imshow('img',img)
    #saving frames
    cv2.imwrite('C:\Users\\ravindra\\Desktop\\intern\\day2-ravi\\output\\'+str(x)+'.jpg',img)
    x=x+1
    #press q to close webcam
    if cv2.waitKey(30) & 0xff==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
