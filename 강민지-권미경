# 연구 결과 보고서
- 프로젝트명: Boogie The Guider
- 작성자: 강민지(wbclair7@konkuk.ac.kr), 권미경(kmk3942@konkuk.ac.kr)
- 작성일: 2020. 02. 26.

## 개요
- 주제: Turtlebot3 Waffle Pi와 Open Manipulator를 이용한 건물 안내로봇
- 목표: 
  - ROS mapping 및 navigation으로 목표 지점까지 이동
  - YOLO를 활용하여 엘리베이터 버튼(화살표, 숫자)을 인식하고 Manipulator로 버튼 누르기
- 성과: YOLO training을 통해 화살표 이미지 detect 성공

## 연구 계획
- 세부 계획
  - 라이다가 매니퓰레이터를 장애물로 인식하는 문제 해결 예정
  - 실시간으로 장애물을 피하여 목표지점으로 도착해야 하도록 개발 예정
  - 엘리베이터 이용 시 영상처리를 통한 층수 인식 및 적정 속도로 승하차하도록 개발 예정

- 로봇 구성 계획
    ![사진](구성도_측면.png)

    - 1층: 액추에이터(바퀴)
    - 2층: 클라이언트 역할을 위한 노트북 (층수를 전달 받을 예정, 코드 실행)
    - 3층: Jetson TX2, 배터리(3cell, 6000mah)
    - 4층: Pocket WIFI(무선라우터 대체), OpenCR, 배터리(3cell, 3700mah), USB camera
    - 5층: LiDAR, Open Manipulator

- 필요 물품
    - 서포터 연장 나사
    - 배터리(3cell,6000mah)
    - USB camera
    - Pocket WIFI
    - Laptop(GPU 탑재)


## 연구 결과
- 기존의 RaspberryPi 대신 Jetson TX2를 Turtlebot에 탑재하여 개발환경 구축(Ubuntu 16.04 / ROS kinetic)
- 259장의 이미지를 YOLO training 후 화살표 이미지 detect 성공
 ![사진](ScreenShot.png)
