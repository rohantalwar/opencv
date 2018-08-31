# OpenCV program to detect face in real time
# import libraries of python OpenCV 
import cv2 as cv 
 
face1 = cv.CascadeClassifier('face.xml')
 

eye1 = cv.CascadeClassifier('eyes.xml') 
 

cap = cv.VideoCapture(0)
 

while (True): 
 
    
    ret, img = cap.read() 
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    faces = face1.detectMultiScale(gray, 1.3, 5)
 
    for (x,y,w,h) in faces:
        
        cv.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2) 
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
 
        
        eyes = eye1.detectMultiScale(roi_gray) 
 
        
        for (ex,ey,ew,eh) in eyes:
            cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,127,255),2)
 
    
    cv.imshow('img',img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
 

cap.release()

cv.destroyAllWindows() 

