import cv2

cap = cv2.VideoCapture(0)
#ret return juste true ou false
while True:
    ret, frame = cap.read()
    cv2.imshow("frame1",frame)
    k=cv2.waitKey(1)
    if k==27:
        break
cv2.destroyAllWindows()
print("frame",frame)
cap.release()
