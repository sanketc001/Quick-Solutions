import cv2
import os
import mediapipe as mp
face_classifier=mp.solutions.face_detection.FaceDetection(0.75)
def matcher(face):
    for facetomatchwith in faces:
        if(face==facetomatchwith):
            return facetomatchwith.name
        else:
            return None
# face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + '/haarcascade_frontalface_default.xml')
images = []
classNames = []
path = 'input_facedetection_labeler'
directory = 'output'
mylist = os.listdir(path)
for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    # curImg=cv2.resize(curImg,(1366,768))
    cv2.imshow("img",curImg)
    cv2.waitKey(1000)
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
    print(path,cl)
    # gray = cv2.cvtColor(curImg, cv2.COLOR_BGR2GRAY)
    # faces = face_classifier.detectMultiScale(gray, 1.9, 10)
    rgb=cv2.cvtColor(curImg, cv2.COLOR_BGR2RGB)
    faces=face_classifier.process(rgb)
    if faces:
        for id,info in enumerate(faces.detections):
            mp.solutions.drawing_utils.draw_detection(rgb,info)
            print(id,info.score[0]*100,info.location_data.relative_bounding_box)
            cv2.imshow("img", rgb)
            cv2.waitKey(10000)
    # if faces != ():
    #     c=1
    #     for (x, y, w, h) in faces:
    #         crop_img = curImg[y:y + h, x:x + w]
    #         if(matcher(crop_img)==None):
    #             pt1 = (y, x)
    #             pt2 = (y+h, x+w)
    #             color = (255, 0, 0)
    #             thickness = 2
    #             lineType = cv2.LINE_4
    #             img_rect = cv2.rectangle(curImg, pt1, pt2, color, thickness, lineType)
    #             text = "Unknown"
    #             org = (400, 30)
    #             fontFace = cv2.FONT_HERSHEY_SIMPLEX
    #             fontScale = 1
    #             color = (0, 255, 25)
    #             lineType = cv2.LINE_4
    #             img_text = cv2.putText(img_rect, text, org, fontFace, fontScale, color, lineType)
    #             cv2.rectangle(curImg,(y,w),(y+h,x+w),cv2.HERSEY_COMPLEX,2)
    #         else:
    #             pt1 = (y, x)
    #             pt2 = (y + h, x + w)
    #             color = (255, 0, 0)
    #             thickness = 2
    #             lineType = cv2.LINE_4
    #             img_rect = cv2.rectangle(curImg, pt1, pt2, color, thickness, lineType)
    #             text = matcher(crop_img)
    #             org = (400, 30)
    #             fontFace = cv2.FONT_HERSHEY_SIMPLEX
    #             fontScale = 1
    #             color = (0, 255, 25)
    #             lineType = cv2.LINE_4
    #             img_text = cv2.putText(img_rect, text, org, fontFace, fontScale, color, lineType)
    #             cv2.rectangle(curImg, (y, w), (y + h, x + w), cv2.HERSEY_COMPLEX, 2)
    #         filename = directory+'\\'+ cl+'_'+str(c)+'.jpg'
    #         print(filename)
    #         cv2.imshow(crop_img,"person"+str(c))
    #         cv2.imwrite(filename, crop_img)
    #         c=c+1