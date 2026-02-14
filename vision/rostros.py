

import cv2


def hay_persona():

    cam = cv2.VideoCapture(0)

    ret, frame = cam.read()

    cam.release()


    if not ret:

        return False


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(

        cv2.data.haarcascades + "haarcascade_frontalface_default.xml"

    )

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)


    return len(faces) > 0

