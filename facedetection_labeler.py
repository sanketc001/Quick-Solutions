import cv2
import os
def matcher(face):
    for facetomatchwith in faces:
        if(face==facetomatch):
            return facetomatchwith.name

face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + '/haarcascade_frontalface_default.xml')
images = []
classNames = []
path = 'input_facedetection_labeler'
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
            if()
            cv2.rectangle(curImg,(y,w),(y+h,x+w),cv2.HERSEY_COMPLEX,2)
            filename = directory+'\\'+ cl+'_'+str(c)+'.jpg'
            print(filename)
            cv2.imshow(crop_img,"person"+str(c))
            cv2.imwrite(filename, crop_img)
            c=c+1