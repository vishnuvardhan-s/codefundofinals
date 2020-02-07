# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 12:51:01 2020

@author: Rag
"""

import face_recognition
import cv2
import time
import database as db

image1_encoding = []
image2_encoding = []
detected = ''
video_capture = cv2.VideoCapture(0)
image1 = face_recognition.load_image_file("image1.jpg")
image1_encoding = face_recognition.face_encodings(image1)[0]
image2 = face_recognition.load_image_file("image2.jpg")
image2_encoding = face_recognition.face_encodings(image2)[0]

known_face_encoding = [
    image1_encoding,
    image2_encoding
]
known_face_names = [
    "BVTR001",
    "BVTR002"
]
face_locations = []
face_names = []
face_encodings = []
process_this_frame = True
flag = 0
while True:
    ret, frame = video_capture.read()
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    if process_this_frame:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                known_face_encoding, face_encoding)
            name = "Unknown"
            if True in matches:
                first_match_index = matches.index(True)
                name = known_face_names[first_match_index]
            face_names.append(name)
            if len(face_names)==1 and "Unknown" not in face_names:
                detected = face_names[0]
                update = {'isVerified':True}
                records = db.connect()
                records.update_one({'voterid':detected},{'$set':update})
                print('Matched')
                time.sleep(2)
                exit
                
    process_this_frame = not process_this_frame
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(frame, (left, bottom - 35),
                      (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left+6, bottom-6),
                    font, 1.0, (255, 255, 255), 1)

    cv2.imshow("Recognizing", frame)
    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

video_capture.release()
cv2.destroyAllWindows()
