from os import listdir
import cv2
imgRech = cv2.imread("../image/retate_img.jpg")
imgRech= cv2.resize(imgRech,(100,100))
exsist=False
for f in listdir("../image/visage/"):
    img=cv2.imread("../image/visage/"+f);
    img= cv2.resize(img,(100,100))
    diff=cv2.subtract(imgRech,img)
    b,g,r= cv2.split(diff)
    if cv2.countNonZero(b)==0 and  cv2.countNonZero(g)==0 and  cv2.countNonZero(r)==0:
        exsist=True
        break
if exsist:
    print("image c'est la méme")
else:
    print("image c'est pas la méme")
cv2.waitKey(0)
cv2.destroyAllWindows()   
    
