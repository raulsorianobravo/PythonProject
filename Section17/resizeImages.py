import cv2
import os
import glob

images2 = os.listdir("./Section17/sample_images (1)")

for image in images2:
    print(image)

images = glob.glob("./Section17/sample_images (1)/*.jpg")

for image in images:
    img = cv2.imread(image, 0)
    rimg = cv2.resize(img, (100,100))

    cv2.imshow("Resize", rimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite(image.replace(".jpg","_r.jpg"), rimg)

    print(image )

 