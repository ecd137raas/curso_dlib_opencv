import sys
import cv2
import dlib

video = cv2.VideoCapture(0)
video.set(3, 640) #largura
video.set(4, 480) #altura

face_cascade = cv2.CascadeClassifier("recursos/haarcascade_frontalface_default.xml")

while True:
    conectado, frame = video.read()
    frame = cv2.flip(frame, 1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    print(len(faces))

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.destroyAllWindows()