import cv2
import os
import urllib.request
import numpy as np
import faceRecognition as fr
from tkinter import *
import os
import pyqrcode
from PIL import Image
import eel


# url="http://192.168.43.1:8080/shot.jpg"
# -----------------------------------------
# root2 = Tk()
# root2.configure(background="white")
# Label(root2, text="ID", font=("times new roman", 30),
#       fg="white", bg="purple", height=2)
# e = Entry(root2)
# e.pack()
# Label(root2, text="Name", font=("times new roman", 30),
#       fg="white", bg="purple", height=2)
# e2 = Entry(root2)
# e2.pack()
# -------------------------------------------
eel.init('assets')


def assure_path_exists(path):
    dir = os.path.dirname(path)
    if not os.path.exists(dir):
        os.makedirs(dir)
#face_id=input('enter your id')


@eel.expose
def clickfun(uid_web, name_web):
    face_id = uid_web
    qr = pyqrcode.create(str(face_id)+"."+str(name_web))
    qr.png(str(face_id)+".png", scale=6)
    img = Image.open(str(face_id)+".png")
    img.transpose(Image.FLIP_LEFT_RIGHT)
    img.save(str(face_id)+".png")

    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    face_detector = cv2.CascadeClassifier(
        'haarcascades/haarcascade_frontalface_default.xml')

    count = 0
    loc = ("training_images/"+str(face_id)+"/")

    assure_path_exists(loc)

    while(True):
        ret, test_img = cap.read()

        # imgResp=urllib.request.urlopen(url)
        # imgResp=urllib.request.urlopen(url)
        # imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
        # test_img=cv2.imdecode(imgNp,-1)
        # _, image_frame = imgResp.read()

        # Convert frame to grayscale
        gray = cv2.cvtColor(test_img, cv2.COLOR_BGR2GRAY)

        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:

            cv2.rectangle(test_img, (x, y), (x+w, y+h), (255, 0, 0), 2)

            count += 1

            cv2.imwrite("training_images/"+str(face_id)+"/" +
                        str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h, x:x+w])

            cv2.imshow('frame', test_img)

        if cv2.waitKey(100) & 0xFF == ord('q'):
            break

        elif count >= 100:
            print("Successfully Captured")
            break

    cv2.destroyAllWindows()


# btn = Button(root2, text="Submit", command=clickfun)
# btn.pack()


# root2.title("Intelligent attendance system ")
# Label(root2, text="ATTENDANCE SYSTEM", font=("times new roman", 30), fg="white", bg="purple", height=2)
# root2.mainloop()
