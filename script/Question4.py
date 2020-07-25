import cv2
img = cv2.imread("../image/visage/3.jpg")
retade = cv2.rotate(img, cv2.ROTATE_180)
cv2.imwrite("../image/retate_img.jpg",retade)
cv2.imshow("retate",retade)
