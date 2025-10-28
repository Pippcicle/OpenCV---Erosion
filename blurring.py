import cv2

image = cv2.imread("PIG.png")

cv2.imshow("pig", image)
cv2.waitKey(0)

# Gaussian Blur - used mostly in machine learning preprocessing steps
gblur = cv2.GaussianBlur(image, (7,7), 10)
cv2.imshow("Gaussian Blur Pig", gblur)
cv2.waitKey(0)

# Median Blur - used in digital processing preserves edges but removes noise
mblur = cv2.medianBlur(image, 17)
cv2.imshow("Median Blur Pig", mblur)
cv2.waitKey(0)

# Bilateral Blur - only sharp edges are preserved here
bblur = cv2.bilateralFilter(image, 57, 75, 75)
cv2.imshow("Bilateral Blur Pig", bblur)
cv2.waitKey(0)

cv2.destroyAllWindows()
