import cv2
from datetime import datetime
import pandas

video = cv2.VideoCapture(0)

first_frame=None
status_list=[None, None]
times = []

df = pandas.DataFrame(columns=["Start","End"])

while True:
    
    check, frame = video.read()

    status = 0

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
        if cv2.contourArea(contour) < 5000:
            continue

        status=1
        (x,y,w,h) = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x,y),(x+w,y+h), (255,0,0),1)
    status_list.append(status)
    
    if status_list[-1] == 1 and status_list[-2] == 0:
        times.append(datetime.now())

    if status_list[-1] == 0 and status_list[-2] == 1:
        times.append(datetime.now())

    cv2.imshow("video",frame)
    cv2.imshow("delta_frame",delta_frame)
    cv2.imshow("thresh_frame",thresh_delta)
    cv2.imshow("thresh_frame2",thresh_delta2)

    key=cv2.waitKey(1)
    if key == ord('q'):
        if status == 1:
            times.append(datetime.now())
        break
    
print(times)

for i in range(0,len(times),2):
    df=df._append({"Start":times[i], "End":times[i+1]}, ignore_index = True)

df.to_csv("Times.csv")
video.release()
cv2.destroyAllWindows()