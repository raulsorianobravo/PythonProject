import cv2

img = cv2.imread("./Section17/galaxy.jpg", 0)

#print(type(img))
print(img.shape)
print(img.ndim)

img2 = cv2.imread("./Section17/galaxy.jpg", 1)
print(img2.shape)
print(img2.ndim)

cv2.imshow("Galaxy", img)
cv2.waitKey(0)

cv2.imshow("Galaxy", img2)

cv2.waitKey(0)
cv2.destroyAllWindows()