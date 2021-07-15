import cv2
import os
# Loads model - use the path to this model inside CV2 Data folder
path = r'C:\users\50s\appdata\local\programs\python\python39\lib\site-packages\cv2\data'
face_cascade = cv2.CascadeClassifier(os.path.join(path, 'haarcascade_frontalface_default.xml'))
# Loads Image
img = cv2.imread('friends.jpg')
# Convert it to gray scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Face detector
faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# Draws a retangle in the faces
for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 2)
# Show results
cv2.imshow('img', img)
cv2.waitKey()