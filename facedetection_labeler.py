import cv2
import os
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + '/haarcascade_frontalface_default.xml')
images = []
classNames = []
path = 'input'
directory = 'output'
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    gray = cv2.cvtColor(curImg, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.01, 90)
    if faces != ():
        c=1
        for (x, y, w, h) in faces:
            crop_img = curImg[y:y + h, x:x + w]
            filename = cl+'_'+str(c)+'.jpg'
            cv2.imwrite(filename, crop_img)
            c=c+1