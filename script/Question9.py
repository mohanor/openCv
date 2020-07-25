#ce programme permet d'afficher les points clés
#(KEY Points) d'une image
import cv2
img = cv2.imread("../image/face.jpeg")
#créer un détcteur (ORB detector)
#nfeatures=100 c'est lz maximum de points clés
orb= cv2.ORB_create()
#detecter les points clés(Key Points)
kp = orb.detect(img)
#Afficher les points clés(draw key points)
img1= cv2.drawKeypoints(img,kp,None)
cv2.imshow("image", img)
cv2.imshow("image1",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
