import cv2
cap = cap = cv2.VideoCapture("../video/02 formation smartphones et education 2015 introduction capteurs - YouTube.MP4")
face = cv2.CascadeClassifier("../haar/haarcascade_frontalface_default.xml")
i=1
while True:
    ret,frame = cap.read()
    if ret == True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face.detectMultiScale(gray,1.1,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),1)
            visage =frame[y:y+h,x:x+w]
            cv2.imwrite("../video/faces"+str(i)+".jpg",visage)
            i=i+1
            cv2.imshow("frame1",frame)
        k=cv2.waitKey(1)
        if(k == 27):
            break
    else:
        break

cv2.destroyAllWindows()
cap.release()
