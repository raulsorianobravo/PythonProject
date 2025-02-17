import cv2

face_cascade = cv2.CascadeClassifier("./Section17/Files/haarcascade_frontalface_default.xml")

img = cv2.imread("./Section17/Files/news.jpg", 1)
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.08, minNeighbors=5)

print(type(faces))
print(faces)

for x,y,w,h in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0), 1)

cv2.imshow("Gray", gray_img)
cv2.waitKey(0)

cv2.imshow("Face", img)
cv2.waitKey(0)

cv2.destroyAllWindows() 