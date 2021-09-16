import cv2
import numpy as np
import PoseModule as pm
import time
import m_protractor as pt


cap = cv2.VideoCapture(0)
pTime = 0
detector = pm.poseDetector()
count = 0
check = True
std = False
countDown = 5
check_start = False

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    if countDown >0:
        print(countDown)
        countDown -= 1
        time.sleep(1)
    elif not check_start and countDown == 0:
        check_start = True
        print("시작!")
    else:
        lmList = detector.findPosition(img, draw=False)
        if lmList:
            if lmList[12] and lmList[14] and lmList[20]:
                point = [(lmList[12][1],lmList[12][2]),
                         (lmList[16][1],lmList[16][2])]
                # 종료조건
                end = [(lmList[22][1],lmList[22][2]),
                         (lmList[21][1],lmList[21][2])]
                if pt.distance_point2(end) <= 3000:
                    print(f"종료! 총 {count}개")
                    break
                # distance
                distance = pt.distance_point2(point)
                cv2.putText(img, str(distance), (80,100), cv2.FONT_HERSHEY_PLAIN, 5,
                            (255, 0, 0), 3)
                # check
                if distance > 100000:
                    check = False
                elif distance < 70000:
                    check = True
                if std != check:
                    if not check:
                        count+=1
                        print(f"count! : {count}")
                    std = check
                cv2.putText(img, str(count), (500, 100), cv2.FONT_HERSHEY_PLAIN, 5,
                            (255, 0, 0), 3)
            cv2.circle(img, (lmList[16][1], lmList[16][2]), 15, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (lmList[12][1], lmList[12][2]), 15, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (lmList[11][1], lmList[11][2]), 15, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (lmList[15][1], lmList[15][2]), 15, (0, 255, 0), cv2.FILLED)


    cv2.imshow("img", img)
    if cv2.waitKey(1) == 27:
        break