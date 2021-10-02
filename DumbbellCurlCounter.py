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
time_s = int(time.time())
countDown = 5
check_start = False
print(countDown)

while True:
    success, img = cap.read()
    img = detector.findPose(img, draw=False)
    if countDown > 0:
        if int(time.time()) > time_s:
            countDown -= 1
            print(countDown)
            time_s = time.time()
    elif not check_start and countDown == 0:
        check_start = True
        print("시작!")
    else:
        lmList = detector.findPosition(img, draw=False)
        if lmList:
            if lmList[12] and lmList[14] and lmList[20]:
                # 종료조건
                end = [(lmList[22][1], lmList[22][2]),
                       (lmList[21][1], lmList[21][2])]
                if pt.distance_point2(end) <= 3000:
                    print(f"종료! 총 {count}개")
                    break
                point = [(lmList[12][1],lmList[12][2]),
                         (lmList[14][1],lmList[14][2]),
                         (lmList[20][1],lmList[20][2])]
                # angle
                angle = pt.protractor_point3(point)
                cv2.putText(img, str(angle), (lmList[14][1]+20, lmList[14][2]-20), cv2.FONT_HERSHEY_PLAIN, 3,
                            (0, 255, 0), 3)
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
                cv2.putText(img, str(count), (60, 60), cv2.FONT_HERSHEY_PLAIN, 5,
                            (0, 255, 0), 3)
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (lmList[12][1], lmList[12][2]), 15, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (lmList[20][1], lmList[20][2]), 15, (0, 255, 0), cv2.FILLED)

    cv2.imshow("img", img)
    if cv2.waitKey(1) == 27:
        break