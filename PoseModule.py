import cv2
import mediapipe as mp
import time

class poseDetector():
    def __init__(self, mode = False, comp = 1, smooth = True, enable_seg = False, smooth_seg = True,
                 detectionCon = 0.5, trackCon=0.5):
        self.mode = mode
        self.comp = comp
        self.smooth = smooth
        self.enable_seg = enable_seg
        self.smooth_seg = smooth_seg
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        # mediapipe
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode, self.comp, self.smooth, self.enable_seg, self.smooth_seg,
                                     self.detectionCon, self.trackCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:

            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
        return img

    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = img.shape
                # print(id, lm)
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (255,0,0), cv2.FILLED)
        return lmList

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = poseDetector()
    while True:
        success, img = cap.read()
        img = detector.findPose(img)
        lmList = detector.findPosition(img, draw=False)
        if lmList:
            print(lmList[14],lmList[12], lmList[20])
            cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (lmList[12][1], lmList[12][2]), 15, (0, 255, 0), cv2.FILLED)
            cv2.circle(img, (lmList[20][1], lmList[20][2]), 15, (0, 255, 0), cv2.FILLED)
        # fps
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                    (255, 0, 0), 3)

        cv2.imshow("img", img)
        if cv2.waitKey(1) == 27:
            break

if __name__ == "__main__":
    main()