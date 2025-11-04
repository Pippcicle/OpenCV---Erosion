import cv2
import os

# Read an image
image = cv2.imread("PIG.png",1)
image1 = cv2.imread("PIG.png",0)
# There are 3 parameters to read an image - 
#cv2.IMREAD_COLOR (1) => Specify to load the image in color
#cv2.IMREAD_GRAYSCALE (0) => Specify to load the image in grayscale / black & white
#cv2.IMREAD_UNCHANGED (-1) => Specify to load the image unchanged

#print an image in different colour formats
#splitting the image in red, blue, green saturations
B,G,R = cv2.split(image)

cv2.imwrite("pigpig.png", image1)
print("image saved successfully")

cv2.imshow("coloured pig", image)
cv2.waitKey(0)
cv2.imshow("grey pig", image1)
cv2.waitKey(0)
cv2.imshow("Blue saturation image", B)
cv2.waitKey(0)
cv2.imshow("Green saturation image", G)
cv2.waitKey(0)
cv2.imshow("Red saturation image", R)
cv2.waitKey(0)

cv2.destroyAllWindows()
