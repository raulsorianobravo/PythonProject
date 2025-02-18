import cv2 

video = cv2.VideoCapture(0)

first_frame=None

while True:
    
    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    gray = cv2.GaussianBlur(gray,(21,21),0)

    #print(check)
    #print(frame)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame,gray)
    thresh_delta = cv2.threshold(delta_frame, 30, 255, cv2.THRESH_BINARY)[1]

    thresh_delta2 = cv2.dilate(thresh_delta, None, iterations=2)

    (cnts,_) = cv2.findContours(thresh_delta.copy(),cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in cnts:
        if cv2.contourArea(contour) < 1000:
            continue

        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w,y+h), (255,0,0),1)


    cv2.imshow("video",frame)
    cv2.imshow("delta_frame",delta_frame)
    cv2.imshow("thresh_frame",thresh_delta)
    cv2.imshow("thresh_frame2",thresh_delta2)

    key=cv2.waitKey(1)
    if key == ord('q'):
        break


video.release()
cv2.destroyAllWindows()