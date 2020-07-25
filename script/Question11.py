import cv2
img1 = cv2.imread("../image/face.jpeg")
img2 = cv2.imread("../image/face.jpeg")
#créer un detecteur : ORB
orb = cv2.ORB_create()
#Détecter les points clés el le d+escripteur
kp1, desc1 = orb.detectAndCompute(img1,None)
kp2,desc2= orb.detectAndCompute(img2,None)
#BFMatcher : fait le matching de deux images, en se basant sur les descripteurs
bf = cv2.BFMatcher()
#Faire le matching : la correspondance
matches = bf.match(desc1,desc2)
#Trier pas distances croissantes
matches=sorted(matches,key=lambda x:x.distance)
img_matche= cv2.drawMatches(img1,kp1,img2,kp2,matches[:20],None)
cv2.imshow("image 1",img1)
cv2.imshow("image 2",img2)
cv2.imshow("image 3",img_matche)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(matches)
