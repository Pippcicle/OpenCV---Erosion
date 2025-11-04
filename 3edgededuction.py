import cv2

pig = cv2.imread('PIG.png')
rabbit = cv2.imread('rabbit.png')
#Canny Edge Detection Algorithm
#The Canny edge detection algorithm is a multi-stage process for identifying edges in images, known for its effectiveness and 
#accuracy. It aims to detect a wide range of edges while minimizing false positives and providing accurate localization.

rabbitedge = cv2.Canny(rabbit, 100,200)
edges = cv2.Canny(pig, 100,200)

cv2.imwrite("Pig edges.png", edges)
cv2.imwrite("Rabbit Edges.png", rabbitedge)
cv2.waitKey(0)
cv2.destroyAllWindows()