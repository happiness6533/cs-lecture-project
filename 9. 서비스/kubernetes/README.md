##############################################################
도커와 컨테이너

도커
컨테이너 기술을 쉽게 사용할 수 있도록 도와주는 프로그램

컨테이너
도커 컨테이너는 도커 이미지를 기반으로 실행되는 프로세스다. 도커 이미지만 있다면 환경의 영향을 받지 않고 다양한 환경에서 컨테이너를 기동시킬 수 있기 때문에 활용성이 높다.

가상머신
운영체제 위에 하드웨어를 에뮬레이션
그 위에 가상 운영체제를 다시 올림
그 위에서 프로세스를 실행

컨테이너
하드웨어 에뮬리에션 없이 리눅스 커널을 공유해서 바로 프로세스를 실행. 컨테이너는 프로세스다. 하지만 컨테이너라고 부르는 이유는 리눅스 커널에 포함된 프로세스 격리 기술들을 사용해서 생성한 특별한 프로세스이기 때문이다.

컨테이너의 원리
원래 하나의 OS 상에서 움직이는 여러 어플리케이션은 똑같은 시스템 리소스를 공유해서  사용한다. 이때 작동하는 여러 어플리케이션은 데이터를 저장하는 디렉토리를 공유하고, 서버에 설정된 동일한 IP 주소로 통신을 한다. 그래서 여러 어플리케이션을 사용하고 있는 미들웨어나 라이브러리의 버전이 다른 경우에는 각 어플리케이션이 서로 영향을 받지 않도록 주의해야 한다.

그러나 컨테이너 기술을 사용하면 OS나 디렉토리, IP 주소 등과 같은 시스템 자원을 마치 각 어플리케이션이 점유하고 있는 것처럼 보이게 할 수 있다. 컨테이너는 훨씬 가볍고 운영체제 커널을 공유하며 시작이 훨씬 빠르고 운영체제 전체 부팅보다 메모리를 훨씬 적게 차지한다. 이를 가능하게 하는 리눅스 커널의 2가지 기능이 cproup과 네임스페이스다

cgroup
단일 또는 테스크 단위의 프로세스 그룹에 대한 자원 할당을 제어하는 커널 모듈

네임스페이스
호스트명, 네트워크, 파일 시스템 마운트, 프로세스 간 통신, 사용자 ID, PID 등의 자원을 격리할 수 있는 리눅스 커널의 기술이다. 네임스페이스로 격리된 내부에서는 외부가 보이지 않기 때문에 컨테이너 내부는 독립된 공간처럼 느껴진다. 이때 네임스페이스로 격리된 프로세스에 메모리, CPU, 네트워크, 장치 입출력 등의 사용량을 할당하고 제한하는데, 이 때 씨그룹 기술을 사용한다. 그리고 이러한 기술을 쉽게 사용할 수 있게 하는 것이 도커이다.
##############################################################
쿠버네티스
##############################################################
젠킨스
##############################################################
