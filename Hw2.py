import cv2
import numpy as np

image1 = cv2.imread("mang.png")
image2 = cv2.imread('RJ.png')
rabbit = cv2.imread("rabbit.png")
cv2.imshow("mang", image1)
cv2.waitKey(0)
cv2.imshow("RJ", image2)
cv2.waitKey(0)

gblur = cv2.GaussianBlur(image1, (7,7), 30)
cv2.imshow("Gaussian Blur Mang", gblur)
cv2.waitKey(0)

mblur = cv2.medianBlur(image1, 37)
cv2.imshow("Median Blur Mang", mblur)
cv2.waitKey(0)

bblur = cv2.bilateralFilter(image1, 100, 75, 75)
cv2.imshow("Bilateral Blur Mang", bblur)
cv2.waitKey(0)

kernel = np.ones((5,5), np.uint )
erosion = cv2.erode(image1, kernel)
cv2.imshow("Eroded Mang", erosion)
cv2.waitKey(0)

resizeRJ = cv2.resize(image2, (120,120))
cv2.imshow("Little RJ", resizeRJ)
cv2.waitKey(0)

resizemang = cv2.resize(image1, (120,120))
cv2.imshow("Little Mang", resizemang)
cv2.waitKey(0)


#0.5 and 0.4 are weights to be multiplied for each pixel, 0 is gamma_value (measurement of light)
image3 = cv2.flip(image2, 1)
weightedSum = cv2.addWeighted (image2, 0.7, image3, 0.3, 0)
cv2.imshow("Weighted Image", weightedSum)
cv2.waitKey(0)

cv2.destroyAllWindows()



