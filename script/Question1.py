import cv2
face_cascade = cv2.CascadeClassifier("../haar/haarcascade_frontalface_default.xml")

img = cv2.imread("../image/messi2.jpg")
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)
i=1
for(x,y,w,h) in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    visage= img[y:y+h,x:x+w]
    i=i+1
cv2.imshow("face",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
