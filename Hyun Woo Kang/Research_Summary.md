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
<b>SBC 업그레이드는 위 주제와 동일합니다.</b><br><br>
ROS Management System은 기본적으로 서버 관리 / 로깅을 진행할 수 있고, ROS Master Host에 연결되어 있는 Slave 노드의 정보를 읽을 수 있게 만든다. 이에 대한 목표는 SBC의 CPU 및 GPU Load정보를 모니터링 하는 것 까지가 목표였으나, 특정 사유로 인해 이는 동시에 진행하지 못하고 Slave노드의 일부 정보만 받는 상태에서 멈추게 되었습니다.<br><br>
아래 링크는 현재까지 동계방학 때 개발한(Deprecated) ROS Manager Github 링크입니다.<br>
[Link to Custom-Dev ROS Manager](https://github.com/KangDroid/ROS_Manager) (Based on C/C++ With QT5)

성과
----
<b>결론: N/A</b> <br>

- ROS2 내부 버전 간의 호환성 이슈<br>
  ROS2는 Master Host와 Slave 서로 버전이 다를 경우 데이터 송/수신에 문제가 생깁니다. 따라서 모두 최신 버전은 ROS2 Master(devel) 브렌치를 사용하지만, arm64에 대한 컴파일 지원이 없었고, 이에 대한 Documentation또한 없었기 때문에 이를 해결하느라 시간이 생각보다 많이 걸렸습니다.
- Cartography | SLAM 주행과 Rviz2의 동시 충돌([Reference](https://github.com/ROBOTIS-GIT/turtlebot3/issues/531))
- CSI Issue<br>
  이는 왜그런지 모르겠으나, CSI관련 ROS노드를 실행 시, Topic은 만들어지지만 Publishing이 안돼는걸 확인했습니다. <br><br>
  기존 Raspberry Pi CSI-Cam은 MMAL 라이브러리를 사용해 자체적인 userland 드라이버를 사용하지만, Jetson은 GStreamer을 이용하는 것으로 확인되었고, CSI노드 실행 시, GStreamer에서 랜덤으로 Pipe Open이 되질 않습니다. 즉, 한번 잘 작동 되고 나서 GStreamer 프로세스가 운영체제에 의해서 죽을 시, 관련 리소스를 unlock시키지 못하는 경우가 있는 것 같습니다.<br><br>
  실제로 ROS를 끼지 않고 단독으로 GStreamer을 실행시키는 경우, 실행은 잘 되지만 프로세스가 죽을때는 무한로딩(Wait)이 되다가 혼자 죽어버리는 경우가 존재하는 것으로 봐써는 Pipe/Resource가 제대로 Unlock되는게 아닌거 같다는 생각이 듭니다.<br><br>
  CSI관련 노드는 CSI-Node --> GStreamer --> GSCam(ROS Official Node)로 이루어지는데, GStreamer 파라미터가 잘못되었거나, GSCam이 Jetson에서 쓰는 GStreamer의 실제 영상 데이터를 못 받아올 확률이 있습니다.