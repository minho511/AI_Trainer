# AI_Trainer
mediapipe.pose, OpenCV를 사용하여 팔굽혀펴기, 아령운동의 개수를 세어주는 프로그램을 만든다.
___
- [mediapipe.pose](https://google.github.io/mediapipe/solutions/pose.html)
<img src="https://google.github.io/mediapipe/images/mobile/pose_tracking_full_body_landmarks.png" width=500>

- AI_Trainer.py
  - 아령을 들었다 내리는 개수를 카운트한다.
  - (12-14-20) 어깨, 팔꿈치, 오른손의 각도를 계산

- AI_Trainer2.py
  - 팔굽혀펴기 개수를 카운트한다.
  - (12-16)어깨와 팔목의 거리를 계산

- 공통
  - (22-21)두 엄지를 모아 프로그램을 종료한다.
  - 프로그램 시작후 5초동안의 준비시간이 있다.
