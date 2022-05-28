from sre_constants import SUCCESS
import cv2
import numpy as np
import face_recognition
import os
import streamlit as st
from datetime import datetime
from deepface import DeepFace
import mysql.connector

st.title("Welcome Dear Employee")
run = st.checkbox('Run')
FRAME_WINDOW = st.image([])
path = 'images'
images = []
personName = []
myList = os.listdir(path)
t=0
s=0
# print(myList)

for cu_img in myList:
    current_img = cv2.imread(f'{path}/{cu_img}')
    images.append(current_img)
    personName.append(os.path.splitext(cu_img)[0])

# print(personName)

def faceEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = faceEncodings(images)
print("All Encodings Completed!!!")

camera = cv2.VideoCapture(0)
print ("Test return value from camera "+ str(camera))
if not camera.isOpened():
    print("Cannot open camera")
    exit()

while run:
    ret, frame = camera.read()

    print ("return value from camera "+ str(ret))
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = cv2.resize(frame, (0,0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(faces)
    encodeCurrentFrame = face_recognition.face_encodings(faces, facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodeCurrentFrame, facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)

        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = personName[matchIndex].upper()

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(frame, (x1,y1),(x2,y2),(0,255,0), 2)
            cv2.rectangle(frame, (x1, y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

            faceCascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
            result=DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
    
            gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces=faceCascade.detectMultiScale(gray,1.1,4)
            
            for(x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0,255,0), 2)
            
            font=cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(frame,
                result['dominant_emotion'],
                (50,50), #offset
                font,3,
                (255,0,0), #bgr, color
                2,
                cv2.LINE_4)

            cv2.imshow('Demo video',frame)
            
            if cv2.waitKey(2) & 0xFF==ord('q'):
                break

            emo=result['dominant_emotion']

            while s<1:
                conn=mysql.connector.connect(host="localhost", user="root", password="", database="newdb")
                cursor=conn.cursor()
                query="select * from emotion"
                cursor.execute(query)
                record=cursor.fetchall()
                for rows in record:
                    if rows[0]==emo:
                        ans=rows[1]
                conn.commit()
                cursor.close()
                conn.close()
                st.write(ans)
                s=s+1


            while t<1:
                conn=mysql.connector.connect(host="localhost", user="root", password="", database="newdb")
                cursor=conn.cursor()
                query="insert into attendance(name,entry_time,emotion) values('{}','{}','{}')".format(name,datetime.now(),emo)
                cursor.execute(query)
                conn.commit()
                cursor.close()
                conn.close()
                t=t+1

    FRAME_WINDOW.image(frame)

else:
    st.write('Stopped')