import mysql.connector

mysql_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'reconnaissance_de_visage',
    'port': '3306',
    'ssl_disabled': True
}

cnx = mysql.connector.connect(**mysql_config)
cursor = cnx.cursor()

cursor.execute("select nom from reconnaissande_de_visage_etudiants where id=8")
n = cursor.fetchone()
n = "+".join(n)
print(str(n))
print(type(n))
cursor.close()


"""import cv2
import os
import face_recognition
import numpy as np

# Load the cascade
face_cascade = cv2.CascadeClassifier('C:\\Users\\dell\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data//haarcascade_frontalface_default.xml')
path = 'E:\\Reconnaissande_de_visage\\media\\images'
images = []
classNames = []
myList = os.listdir(path)

for list in myList:
    curImg = cv2.imread(f'{path}/{list}')
    images.append(curImg)
    #classNames.append(os.path.splitext(list)[0])
    classNames=myList
#print(curImg)

def findEncodings(images):
    encodeList =  []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


encodeListKnown = findEncodings(images)
# To capture video from webcam.
cap = cv2.VideoCapture(0)
# To use a video file as input
# cap = cv2.VideoCapture('filename.mp4')

while True:
    # Read the frame
    _, img = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, "Introuvable", (x + 6, y - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)
    # Display
    cv2.imshow('Webcam', img)

    # Stop if escape key is pressed
    k = cv2.waitKey(30)
    if k==27:
        break

# Release the VideoCapture object
cap.release()"""