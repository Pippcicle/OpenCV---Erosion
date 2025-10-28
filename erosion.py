import cv2
import numpy as np

image = cv2.imread("PIG.png")

cv2.imshow("pig", image)
cv2.waitKey(0)

#A kernel, also known as a structuring element, is a small matrix used in image processing to define the 
#neighborhood for an erosion operation. It determines which pixels are eroded (removed) from the boundaries 
#of objects in an image

#uint = unsigned integer 8-bit

kernel = np.ones((5,5), np.uint )
erosion = cv2.erode(image, kernel)
cv2.imshow("Eroded Pig", erosion)
cv2.waitKey(0)


cv2.destroyAllWindows()