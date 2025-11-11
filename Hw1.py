import cv2
import os

image = cv2.imread("mang.png",1)
image1 = cv2.imread("mang.png",0)

B,G,R = cv2.split(image)

cv2.imwrite("maaaang.png", image1)
print("image saved")

cv2.imshow("normal mang", image)
cv2.waitKey(0)
cv2.imshow("greyed mang", image1)
cv2.waitKey(0)
cv2.imshow("Blue mang", B)
cv2.waitKey(0)
cv2.imshow("Green mang", G)
cv2.waitKey(0)
cv2.imshow("Red mang", R)
cv2.waitKey(0)

cv2.destroyAllWindows()
 