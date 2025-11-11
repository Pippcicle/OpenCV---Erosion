import cv2

mang = cv2.imread('mang.png')
RJ = cv2.imread('RJ.png')

rjedge = cv2.Canny(RJ, 100,200)
mangedge = cv2.Canny(mang, 100,200)

cv2.imwrite("Mang edges.png", mangedge)
cv2.imwrite("RJ Edges.png", rjedge)
cv2.waitKey(0)

hsvimage = cv2.cvtColor(mang, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV MANG", hsvimage)
hsvimage = cv2.cvtColor(RJ, cv2.COLOR_BGR2HSV)
cv2.imshow("HSV RJ", hsvimage)
cv2.waitKey(0)

rows,columns = RJ.shape[:2]
rotatedRJ = cv2.getRotationMatrix2D((columns/2,rows/2), 78, 1)
resolution = cv2.warpAffine(RJ, rotatedRJ, (columns, rows))
cv2.imshow("rotated RJ", resolution)
cv2.waitKey(0)

cv2.destroyAllWindows()