import cv2 

video = cv2.VideoCapture(0)

fps= 1

while True:
    
    fps+=1
    check, frame = video.read()

    #print(check)
    #print(frame)



    cv2.imshow("video",frame)
    
    key=cv2.waitKey(1)
    if key == ord('q'):
        break

print(fps)
video.release()
cv2.destroyAllWindows()