import cv2
img1 = cv2.imread("../image/messi2.jpg")
img2 = cv2.imread("../image/messi2.jpg")
#créer un detecteur : ORB
orb = cv2.ORB_create()
#Détecter les points clés el le d+escripteur
kp1, desc1 = orb.detectAndCompute(img1,None)
kp2,desc2= orb.detectAndCompute(img2,None)
#BFMatcher : fait le matching de deux images, en se basant sur les descripteurs
bf = cv2.BFMatcher()
#Faire le matching : la correspondance
matches = bf.knnMatch(desc1,desc2,k=2)
meilleurs_points=[]
for m, n in matches:
    if m.distance<0.6*n.distance:
        meilleurs_points.append(m)

pourcentage = (len(meilleurs_points)/len(kp1))*100
print("pourcentage:",pourcentage)
img_matche= cv2.drawMatches(img1,kp1,img2,kp2,meilleurs_points,None)
cv2.imshow("image 1",img1)
cv2.imshow("image 2",img2)
cv2.imshow("image 3",img_matche)
cv2.waitKey(0)
cv2.destroyAllWindows()

