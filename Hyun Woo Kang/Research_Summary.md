연구 결과 보고서
================
- 작성자: 강현우 - Jason H.W Kang, Aka KangDroid (kangdroid@konkuk.ac.kr)
- 작성일: 2020.02.26

개요
====

주제:
-----
- TB3 Burger에 대해 SBC 업그레이드(Raspberry Pi 3B+ --> NVidia Jetson Nano)
- ROS Management System(군집운행)

목표
----
SBC 업그레이드는 위 주제와 동일함.<br>
ROS Management System은 기본적으로 서버 관리 / 로깅을 진행할 수 있고, ROS Master Host에 연결되어 있는 Slave 노드의 정보를 읽을 수 있게 만든다. 이에 대한 목표는 SBC의 CPU 및 GPU Load정보를 모니터링 하는 것 까지가 목표였으나, 특정 사유로 인해 이는 동시에 진행하지 못하고 Slave노드의 일부 정보만 받는 상태에서 멈추게 되었다.<br>
[Link to Custom-Dev ROS Manager](https://github.com/KangDroid/ROS_Manager) (Based on C/C++ With QT5)

성과
----
<b>결론: N/A</b> <br>
ROS2의 불안정성 및 내부 Platform API 미정립(Cannot Migrate ROS1 Driver to ROS2.)<br>
Jetson Nano의 CSI-Cam: Lock/Pipe 문제?(자세한 것은 PPT참조 부탁드립니다.)