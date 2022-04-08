from cv2 import cv2
import os
import face_recognition
import numpy as np
import mysql.connector
from mysql.connector import Error

path = 'E:\\Reconnaissande_de_visage\\media\\images'
images = []
classNames = []
myList = os.listdir(path)
#print(myList)

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

cap = cv2.VideoCapture(0)
def detect():
    while True:
        success, img = cap.read()

        imgS = cv2.resize(img,(0,0), None, 0.25, 0.25)
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

        facesCurFrame = face_recognition.face_locations(imgS)
        encodeCurframe = face_recognition.face_encodings(imgS,facesCurFrame)

        for encodeFace, faceLoc in zip(encodeCurframe,facesCurFrame):
            matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
            faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
            #print(faceDis)

            matchIndex = np.argmin(faceDis)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

            if matches[matchIndex]:
                name = classNames[matchIndex] #.upper()
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

                str1 = "images/"
                photo = "".join((str1, name))
                #print("phot="+photo)
                cursor.execute(f"select nom from reconnaissande_de_visage_etudiants where photo = '{photo}'")
                n = cursor.fetchone()
                n = "+".join(n)
                #print(n)
                cursor.close()
                """except Error as e:
                    print("mysql DB connection error")
                    print(e)"""

                #cv2.rectangle(img,(x1,y1-35),(x2,y2),(0,255,0),cv2.FILLED)
                cv2.putText(img,n,(x1+6,y1-6),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
            else:

                cv2.putText(img,"Inconnu", (x1 + 6, y1 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow('WebCam',img)
        k = cv2.waitKey(30)
        if k == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

detect()