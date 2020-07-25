import cv2

cap = cv2.VideoCapture("../video/02 formation smartphones et education 2015 introduction capteurs - YouTube.MP4")
#ret return juste true ou false
while True:
    ret, frame = cap.read()
    if ret == True:
        cv2.imshow("frame1",frame)
        k=cv2.waitKey(1)
        if k==27:
            break
    else:
        break
    

   

cv2.destroyAllWindows()
print("return",ret)
print("frame",frame)
cap.release()
