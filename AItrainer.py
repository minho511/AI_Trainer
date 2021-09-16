import cv2
import numpy as np
import PoseModule as pm
import time
import m_protractor as pt

cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()
count = 0
check = False
std = False
# count down
countDown = 5
while countDown!=0 :
    print(countDown)
    countDown -= 1
    time.sleep(1)
print("시작!")

while True:
    success, img = cap.read()
    img = detector.findPose(img, draw=False)
    lmList = detector.findPosition(img, draw=False)
    if lmList:
        if lmList[12] and lmList[14] and lmList[20]:
            point = [(lmList[12][1],lmList[12][2]),
                     (lmList[14][1],lmList[14][2]),
                     (lmList[20][1],lmList[20][2])]
            # angle
            angle = pt.protractor_point3(point)
            cv2.putText(img, str(angle), (80,100), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 3)
            # check
            if angle > 160:
                check = True
            elif angle <50:
                check = False
            if std != check:
                if not check:
                    count+=1
                    print(f"count! : {count}")
                std = check
            cv2.putText(img, str(count), (500, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                        (255, 0, 0), 3)
        cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (lmList[12][1], lmList[12][2]), 15, (0, 255, 0), cv2.FILLED)
        cv2.circle(img, (lmList[20][1], lmList[20][2]), 15, (0, 255, 0), cv2.FILLED)




    cv2.imshow("img", img)
    if cv2.waitKey(1) == 27:
        break