import cv2
import numpy as np
from PIL import Image
import pickle
import peopledb
peopleDB = peopledb.PeopleDB()

faceDetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cam = cv2.VideoCapture(0)
rec = cv2.face.LBPHFaceRecognizer_create()
rec.read("recognizer\\trainningData.yml")
id = 0
# set text style
fontface = cv2.FONT_HERSHEY_SIMPLEX
fontscale = 1
fontcolor = (203, 23, 252)

# get data from sqlite by ID


def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)


while(True):
    # camera read

    ret, img = cam.read()
    # img = cv2.imread("ImageTrain/a.jpg")
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceDetect.detectMultiScale(gray, 1.3, 5)
    for(x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        id, conf = rec.predict(gray[y:y+h, x:x+w])
        print(id)
        profile = peopleDB.getByID(id)
        # set text to window
        if(profile != None):
            # cv2.PutText(cv2.fromarray(img),str(id),(x+y+h),font,(0,0,255),2);
            cv2.putText(
                img, "Name: " + str(profile[1]), (x, y+h+30), fontface, fontscale, fontcolor, 2)
            cv2.putText(
                img, "Age: " + str(profile[2]), (x, y+h+60), fontface, fontscale, fontcolor, 2)
            cv2.putText(
                img, "Gender: " + str(profile[3]), (x, y+h+90), fontface, fontscale, fontcolor, 2)
    cv2.imshow('Face', ResizeWithAspectRatio(img, height=900))
    if cv2.waitKey(1) == ord('q'):
        break
cam.release()
cv2.destroyAllWindows()
