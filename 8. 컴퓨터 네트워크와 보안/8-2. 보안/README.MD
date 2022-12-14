## 보안
##############################################################
보안의 1번째 핵심. 암호화를 통한 기밀성 유지
대칭키 방식
암호화와 복호화에 동일한 키를 사용하는 보안 방식
메세지를 대칭키로 암호화하고 전송
암호화된 메세지를 받고 대칭키로 복호화
암호화된 메세지와 키를 함께 전송해야 하기 때문에 키를 해커가 가로채는 경우 기밀성 / 무결성 위험


N개의 서로 다른 노드에 키를 분배하려면 N(N - 1) / 2만큼의 키가 필요하고 키가 사전에 분배되어야 한다
예시: DES(블록 길이 64비트) / 3-DES(블록 길이 64비트) / AES(블록 길이 128비트)
예시: ECB 모드(평문 블록과 암호 블록이 일대일 관계를 유지) / CBC 모드(한 단계 앞에서 수행된 암호문 블록과 평문 블록을 XOR한 후 암호화를 수행)
예시: IPSec은 3DES-CBC, AES-CBC 사용
##############################################################
비대칭키 방식
방식1 - 공개키로 암호화 / 개인키로 복호화
받는 사람이 공개키와 개인키를 생성
메세지를 받는 사람이 만든 공개키로 암호화하고 전송
암호화된 메세지를 받으면 받는 사람의 개인키로 복호화

방식2 - 개인키로 암호화 / 공개키로 복호화
보내는 사람이 공개키와 개인키를 생성
메세지를 보내는 사람의 개인키로 암호화하고 전송
암호화된 메세지를 받은 사람이 보낸 사람의 공개키로 복호화

해커가 공개키와 개인키를 모두 미리 위조하고 메세지를 변조하고 공개키로 암호화하면 기밀성 / 무결성 위험
거듭제곱과 큰 소수를 이용한 연산을 주로 이용하므로 계산 속도가 느리며 전자 상거래 및 인터넷 뱅킹에 사용된다
N개의 서로 다른 노드에 키를 분배하려면 2N개가 필요하다
예시: Diffie-Hellman / RSA
##############################################################
RSA 비대칭키 방식 이해 - 단방향 암호화 방식 - 무결성을 검증할 때 사용한다
서버에서 두 개의 소수 p, q를 선택한다
파이n = (p - 1) * (q - 1)과 서로소인 공개키 kp를 결정한다
(kp * ks) mod 파이(n) = 1을 만족하는 개인키 ks를 결정한다
두 소수의 곱 N을 계산한다
kp와 N을 공개한다
암호화: 평문 P를 공개키 kp로 거듭제곱 한 후에 N으로 나눈 나머지로 암호화한다
복호화: 암호문 C를 개인키 ks로 거듭제곱 한 후에 N으로 나눈 나머지로 복호화한다
만약 N과 kp를 가지고 ks를 알아낼 수 있다면 암호가 깨지게 되지만 소수의 분해가 어렵기 때문에 이를 방지할 수 있다
만약을 위해 두 소수의 곱 N은 1024비트 길이를 사용한다
##############################################################
Diffie-Hellman 비대칭키 방식 이해 - 양방향 암호화 방식 - 기밀성과 무결성이 모두 필요할 때 사용한다
데이터를 주고 받을 2개의 노드가 모두 공유하는 전역 변수인 소수 p와 p의 원시근 r을 선택한다
노드 a는 p보다 작은 비밀 양의 정수 a를 선택해서 r의 a제곱을 p로 나눈 나머지를 공개키 ya로 선택한다
노드 b도 마찬가지 방식으로 공개키 yb를 선택한다
이제 두 노드가 공개키를 교환한다
노드 a는 노드b의 공개키 yb를 자신의 비밀 양의 정수 a로 거듭제곱하고 p로 나눈 나머지를 자신의 비밀키 K로 결정한다
노드 b는 노드a의 공개키 ya를 자신의 비밀 양의 정수 b로 거듭제곱하고 p로 나눈 나머지를 자신의 비밀키 K로 결정한다
모듈러 연산의 특징에 의해 양쪽의 비밀키 K가 동일해진다
공개키로 비밀 정수를 알아내는 것이 대수적으로 불가능하다
문제는 애초에 처음부터 공개키를 교환하는 과정에서 해커가 관여하면 해커에 의한 서로 다른 비밀키 K1 K2가 생성된다
이를 위해 인증된 Diffie-Hellman 비대칭키 방식을 사용한다
##############################################################
인증된 Diffie-Hellman 비대칭키 방식 이해
애초에 처음에 공개키를 생성하고 전달할 때 무결성을 위해서 전자서명을 하고 상대에게 보낸다...어떻게...? 이제 나옴
##############################################################
보안의 1번째 핵심. 인증을 통한 무결성 유지
해쉬함수
인증을 위해 사용된다
메시지를 일정 길이의 블록(예, 512비트)으로 분할 후 해쉬 함수에 입력☞짧고 일정한 길이의 메시지 다이제스트 생성)
예시: MD5, SHA-1
계산 효율이 좋아야 / 일방향성 / 강한 충돌 회피성
SHA: Secure Hash Algorithm / 뒤에 넘버링은 블럭 길이와 다이제스트 길이에 따라 다름
##############################################################
인증 방법1
대칭키 암호 기반(DES)의 메시지 인증
보내고자 하는 메세지에 해쉬 함수를 적용해서 메세지 다이제스트를 만든다
사전에 교환되어 있는 대칭키 키로 메세지 다이제스트를 암호화해서 메세지 인증 코드를 생성한다
메세지와 인증코드를 전송한다
받는 사람은 받은 메세지에 해쉬함수를 적용해서 메세지 다이제스트를 만든다
받은 메세지 인증 코드를 사전에 교환되어 있던 대칭키로 복호화해서 메세지 다이제스트를 확인한다
두 메세지 다이제스트가 일치한다면 개인키가 안전했다는 가정 아래에


메세지를 보낸 사람이 나와 같은 개인키를 가지고 있다는 무결성을 보장한다
메세지가 중간에 변조되지 않았다는 무결성을 보장한다
전체 메세지의 무결성을 해쉬 결과인 다이제스트 메세지에만 암호 알고리즘을 적용해서 속도가 빠르다
##############################################################
인증 방법2
공개키 기반(RSA)의 메세지 인증
보내고자 하는 메세지에 해쉬 함수를 적용해서 메세지 다이제스트를 만든다
메세지를 보내는 사람의 개인키로 메세지 다이제스트를 암호화해서 메세지 인증 코드를 생성한다
메세지와 인증코드를 전송한다
받는 사람은 받은 메세지에 해쉬함수를 적용해서 메세지 다이제스트를 만든다
받은 메세지 인증 코드를 메세지를 보낸 사람의 공개키로 복호화해서 메세지 다이제스트를 확인한다
두 메세지 다이제스트가 일치한다면 공개키가 안전했다는 가정 아래에


메세지를 보낸 사람이 내가 사용한 공개키를 만든 사람이라는 결성을 보장한다
메세지가 중간에 변조되지 않았다는 무결성을 보장한다
전체 메세지의 무결성을 해쉬 결과인 다이제스트 메세지에만 암호 알고리즘을 적용해서 속도가 빠르다
##############################################################
인증 방법3
공유 비밀키 기반(Diffie-Hellman)의 메세지 인증 = HMAC(HMAC-MD5, HMAC-SHA-1은 IPSEC의 인증 기능에 사용되는필수 알고리즘)
https 프로토콜의 핸드쉐이크등에 의해 공유 대칭키를 이미 공유했다고 가정하자.
이제 보내고자 하는 메세지에 비밀키를 포함시킨다 (비밀키 + 메세지)
전체에 해쉬 함수를 적용해서 메세지 다이제스트를 만든다
비밀키를 제외한 메세지와 메세지 다이제스트를 전송한다


받는 사람은 받은 메세지에 사전 공유된 비밀키를 추가해서 해쉬함수를 적용하고 메세지 다이제스트를 만든다
만들어진 메세지 다이제스트가 받은 메세제 다이제스트와 일치하는지 확인한다
두 메세지 다이제스트가 일치한다면 사전 공유된 비밀키가 안전했다는 가정 아래에
메세지를 보낸 사람이 내가 사용한 비밀키를 가진 사람이라는 무결성 보장한다
메세지가 중간에 변조되지 않았다는 무결성을 보장한다
전체 메세지의 무결성을 해쉬 결과인 다이제스트 메세지에만 암호 알고리즘을 적용해서 속도가 빠르다
##############################################################
공개키를 신뢰하기 위한 인프라 구조
개인의 공개키와 개인 정보를 인증기관에 인증서로 등록

개인의 공개키를 어떻게 믿을까?
개인의 인증서 = 개인의 공개키 + 인증기관의 개인키로 서명(예시: X.509, PKIX)
이 인증서는 인증기관의 공개키로만 해독이 가능하기 때문에 인증기관의 공개키가 진짜라면 인증서가 인증된다


그러면 인증 기관의 공개키를 어떻게 믿는가?
인증기관의 인증서 = 인증기관의 공개키 + 상위 인증기관의 개인키로 서명
이제 반복…


최상위 인증기관의 개인키는 엄격한 보안이 요구
##############################################################
기밀성과 무결성을 모두 종합한 실제 대표적인 인터넷 보안 프로토콜
1. IPSec: 키관리(ISAKMP), 인증헤더(AH), 캡슐화 보안 페이로드(ESP) 및 압축 프로토콜
2. SSL(Secure Socket Layer): 웹 서버와 브라우저 사이의 안전한 통신을 위해 개발됨, 서버/클라이언트 인증, 기밀성 보장, HTTPS에 적용
##############################################################
IPSec
암호화를 통한 기밀성을 제공
인증 코드를 통한 IP 패킷의 인증을 통한 무결성도 제공
재전송된 패킷의 감지 및 폐기

네트워크 계층에서 적용되므로 트랜스포트레이어와 어플리케이션 레이어에서는 이미 보안이 보장된다

기존의 IP 계층 바로 아래에 IPSec을 추가적으로 구현(IPV6은 인증헤더(인증)와 ESP헤더(암호화)를 삽입하는 방식으로 해결)

보안연계 (SA: Security Association) : IP 보안 프로토콜, 프로토콜의운용모드, 보안 알고리즘, 보안 키와 키의 수명 등에 대한 통신 쌍방 간의합의 : 인증헤더(AH) 보안연계 / 캡슐화 보안 페이로드(ESP) 보안연계 / 압축(IPComp) 보안연계
트랜스포트 모드
호스트와 호스트 간의 보안 연계
원래 IP 헤더의 발신지 및 목적지 주소를 그대로 유지
터널 모드
보안 게이트웨이와 보안 게이트웨이 사이 or 호스트와 보안 게이트웨이 사이
보안 게이트웨이에서 IPSec 프로토콜 구현
새로운 IP 헤더를 만들어 원래의 IP 패킷을 모두 페이로드화
보안 정책 데이터베이스(SPD) :
IP 패킷의 선택자 정보를 이용하여 IP 패킷에 IPSec 적용 여부 판단
패킷에 IPSec 을 적용하는 경우 보안 연계 데이터베이스의 관련 항목 지정
IPSec 적용 여부를 결정하기 위해 하나 이상의 선택자 정보를 이용
발신지 및 목저지 IP 주소
전송 계층 프로토콜 종류
etc...
지시자 : 선택자들과 일치하는 IP 패킷의 폐기, 통과 또는 IPSec 처리를 지시
IPSec 처리가 요구되는 경우 보안 연계 데이터베이스의 관련 항목을 지정
보안 연계 데이터베이스(SAD) : 보안 연계와 관련된 암호 및 인증 알고리즘과 키 값 등의 매개변수 저장
터널 모드 적용 구간: 보안 게이트웨이와 보안 게이트웨이 사이 또는 호스트와 보안 게이트웨이 사이 로컬 네트워크의 호스트들을 대신하여 보안 게이트웨이에 IPSec 프로토콜 구현l 새로운 IP 헤더를 만들어 원래의 IP 패킷을 모두 페이로드화 함
ISAKMP 프로토콜: 보안연계의 설정 및 해제 기능 담당 키 생성 / 분배 / 관리
AH 및 ESP 프로토콜 AH(인증 헤더) 프로토콜: 패킷의 근원에 대한 인증과 전송 중에 변조되지 않았음을 보장하는무결성 서비스 제공 ESP(캡슐화 보안 페이로드) 프로토콜: IP 패킷의 기밀성 제공을 위한 암호화 기능과 무결성및 인증 기능 제공 인증 및 무결성 서비스: HMAC-MD5, HMAC-SHA-1 기밀성 서비스: 3DES-CBC, AES-CBC
IPComp 프로토콜: IP 보안 프로토콜의 사용으로 증가되는 IP 패킷의 길이를 감소시켜 대역폭 사용의 효율성을높임
##############################################################SSL(http vs https)
TCP 연결을 위한 3-Way Handshake를 먼저 수행한다.
이제 https임을 확인하고 다음 절차를 거친다
내가 사이트에 보내는 정보들을 제 3자가 못 보게 한다.
네이버 서버는 이 두 키들 중 하나는 비밀로 보관하고(개인키)
다른 하나를 그냥 공개한다. 
클라이언트는 서버의 공개키로 비밀번호를 암호화해서 네이버에 보낸다. 누가 가로채도 같은 공개키로는 이 암호문을 풀어낼 수가 없다. 이걸 볼 수 있는 건 이 개인키를 가진 네이버 뿐인 것. 이 경우 공개키는 기밀성을 위해 쓰였다. 그러나 아래에서는 기밀성을 위해서도 사용된다.
접속한 사이트가 믿을 만한 곳인지를 알려준다.
네이버에서 우리에게 보내는 정보들 중
일부는 네이버의 개인키로 암호화가 돼있다.
우리가 네이버의 공개키로 풀어서 알아볼 수 있는 건 네이버의 개인키로 암호화된 정보들 뿐이다. 네이놈에서 온 정보들은 네이버의 공개키로 풀리지 않기 때문에 네이버의 공개키로 열어보려 하면 오류가 난다. 만약 네이버의 공개키만 누군가 확실하게 보장해준다면 이걸 기준으로 안전하게 네이버를 이용할 수 있을 것이다. 이걸 인증해주는 공인된 민간기업들이 있다. 그것이 바로 Certificate Authority 줄여서 CA라고 불린다. 아무나 차려서 될 수 있는 게 아니라 엄격한 인증과정을 거쳐야 CA를 할 수 있다.
우리들의 브라우저, 즉 크롬이나 사파리, 파이어폭스, 엣지, 익스플로러 등에 프로그램에는 이 CA들의 목록이 내장돼 있다. 이 브라우저에서 네이버에 접속할 때 어떤 과정들을 거치게 되는지 살펴보자. 
4. 클라이언트는 아직 이 서버를 신뢰하지 못한다. 그래서 이 둘은 먼저 일종의 탐색과정을 거치게 된다. 이것을 handshake라고 한다. 
먼저 클라이언트는 어떤 랜덤 데이터를 생성하고 그 랜덤 데이터와 브라우저에서 제공하는 암호화 기법을 서버에 보낸다.
만약 이전에 SSL 핸드 쉐이크가 완료된 상태라면, 그때 생성된 세션 아이디(Session ID)도 보낸다
 
이것을 받은 서버는 답변으로 역시 서버측에서 생성한 무작위의 데이터, Server가 결정한 암호화 기법 그리고 해당 서버의 인증서를 실어 보낸다.
자 그럼 이제 이 클라이언트는 이 인증서가 진짜인지 브라우저에 내장된 CA들의 정보를 통해 확인하게 된다.
서버에서 보낸 인증서가 정말 CA의 인증을 받은 인증서라면 해당 CA의 개인키로 암호화가 돼있다. 이제 브라우저에 저장된 CA의 공개키로 이 인증서를 복호화한다. 이 공개키로 복호화될 수 있는 인증서를 발급할 수 있는건 그에 대응하는 개인키를 가진 이 CA 뿐이다. 그렇게 성공적으로 복호화된 인증서에는 이 서버의 공개키가 포함돼있다. 
이렇게 얻어진 신뢰 가능한 서버의 공개키를 이용해서 이제 대칭키를 생성한다.비대칭키 방식으로 메시지를 암호화 및 복호화하는 건 대칭키로 할 때보다 컴퓨터에 훨씬 큰 부담을 주기 때문이다! 대칭키를 공유하는 것을 공개키 방식으로 하게 되면 비밀리에 대칭키를 공유할 수 있게 된다.
공개키를 얻기 전에 서로가 각자 생성한 두 무작위 데이터를 클라이언트는 혼합해서 어떤 임시 키를 만든다. 이 임시 키를 premaster secret 키라고 부른다. 이 키를 서버의 공개키로 암호화해서 서버로 보낸다. 서버에서 이 데이터를 자신의 개인키로 풀고 특정한 함수를 통과시켜서 마스터키라고 부르는 대칭키가 만들어지는 것이다. 이 키를 기본적으로 https의 세션키로 사용하게 된다. 
HTTPS 통신이 완료되는 시점에서 서로에게 공유된 세션 키를 폐기한다. 만약 세션이 여전히 유지되고 있다면 브라우저는 SSL handshake 요청이 아닌 세션 ID만 서버에게 알려주면 된다.
##############################################################
비밀번호 암호화
SHA-256과 같은 해시 함수를 사용해 패스워드를 암호화해 저장하고 값을 비교하는 것은 두 가지 문제점이 있다.

인식 가능성(recognizability)
동일한 메시지가 언제나 동일한 다이제스트를 갖는다면, 공격자가 전처리(pre-computing)된 다이제스트를 가능한 한 많이 확보한 다음 이를 탈취한 다이제스트와 비교해 원본 메시지를 찾아내거나 동일한 효과의 메시지를 찾을 수 있다. 이와 같은 다이제스트 목록을 레인보우 테이블(rainbow table)이라 하고, 이와 같은 공격 방식을 레인보우 공격(rainbow attack)이라 한다.

속도(speed)
해시 함수는 암호학에서 널리 사용되지만 원래 패스워드를 저장하기 위해서 설계된 것이 아니라 짧은 시간에 데이터를 검색하기 위해 설계된 것이다. 바로 여기에서 문제가 발생한다. 해시 함수의 빠른 처리 속도로 인해 공격자는 매우 빠른 속도로 임의의 문자열의 다이제스트와 해킹할 대상의 다이제스트를 비교할 수 있다.(MD5를 사용한 경우 일반적인 장비를 이용하여 1초당 56억 개의 다이제스트를 대입할 수 있다.

단방향 해시 함수 보완하려면 솔팅을 사용한다. 솔트(salt)는 단방향 해시 함수에서 다이제스트를 생성할 때 추가되는 바이트 단위의 임의의 문자열이다. 그리고 이 원본 메시지에 문자열을 추가하여 다이제스트를 생성하는 것을 솔팅(salting)이라 한다. 사용자별로 다른 솔트를 사용한다면 동일한 패스워드를 사용하는 사용자의 다이제스트가 다르게 생성되어 인식 가능성 문제가 크게 개선된다. 솔트와 패스워드의 다이제스트를 데이터베이스에 저장하고, 사용자가 로그인할 때 입력한 패스워드를 해시하여 일치 여부를 확인할 수 있다. 이 방법을 사용할 때에는 모든 패스워드가 고유의 솔트를 갖고 솔트의 길이는 32바이트 이상이어야 솔트와 다이제스트를 추측하기 어렵다.

또한 키 스트레칭(key stretching)도 활용된다. 입력한 패스워드의 다이제스트를 생성하고, 생성된 다이제스트를 입력 값으로 하여 다이제스트를 생성하고, 또 이를 반복하는 방법으로 다이제스트를 생성할 수도 있다. 이렇게 하면 입력한 패스워드를 동일한 횟수만큼 해시해야만 입력한 패스워드의 일치 여부를 확인할 수 있다. 키 스트레칭을 적용하여 동일한 장비에서 1초에 5번 정도만 비교할 수 있게 한다.
GPU를 사용하더라도 수백에서 수천 번 정도만 비교할 수 있다. 50억 번과는 비교할 수도 없을 정도로 적은 횟수다. 앞으로 컴퓨터 성능이 더 향상되면 몇 번의 반복을 추가하여 보완할 수 있다.

권장하는 대표적인 암호화 모듈
PBKDF2
가장 많이 사용되는 key derivation function은 PBKDF2(Password-Based Key Derivation Function)이다. 해시 함수의 컨테이너인 PBKDF2는 솔트를 적용한 후 해시 함수의 반복 횟수를 임의로 선택할 수 있다. PBKDF2는 아주 가볍고 구현하기 쉬우며, SHA와 같이 검증된 해시 함수만을 사용한다. PBKDF2는 NIST(미국표준기술연구소)에 의해서 승인된 알고리즘이고, 미국 정부 시스템에서도 사용자 패스워드의 암호화된 다이제스트를 생성할 때 사용한다.

bcrypt
bcrypt는 애초부터 패스워드 저장을 목적으로 설계되었다. 1999년 발표했고 현재까지 사용되는 가장 강력한 해시 메커니즘 중 하나이다. bcrypt는 보안에 집착하기로 유명한 OpenBSD에서 암호 인증 메커니즘으로 사용되고 있고 미래에 PBKDF2보다 더 경쟁력이 있다고 여겨진다. 
##############################################################
해커들의 전략들
파라미터 변조
xss = cross site scripting = 남들이 보는 게시판(사이트)에 스크립트 집어넣기 => html 내부에 이걸 진짜 js 코드로 인식해서 실행을 해버릴지도
sql 인젝션
 

- 대칭키 방식<br>
  암호화와 복호화에 동일한 키를 사용하는 보안 방식<br>
  메세지를 대칭키로 암호화하고 전송<br>
  암호화된 메세지를 받고 대칭키로 복호화<br>
  암호화된 메세지와 키를 함께 전송해야 하기 때문에 키를 해커가 가로채는 경우 기밀성 / 무결성 위험<br>
  기본 연산을 주로 이용하므로 계산 시간이 빠르며 고속 처리가 필요한 IP 보안 프로토콜에 사용된다<br>
  N개의 서로 다른 노드에 키를 분배하려면 N(N - 1) / 2만큼의 키가 필요하고 키가 사전에 분배되어야 한다<br>
  예시: DES(블록 길이 64비트) / 3-DES(블록 길이 64비트) / AES(블록 길이 128비트)<br>
  예시: ECB 모드(평문 블록과 암호 블록이 일대일 관계를 유지) / CBC 모드(한 단계 앞에서 수행된 암호문 블록과 평문 블록을 XOR한 후 암호화를 수행)<br>
  예시: IPSec은 3DES-CBC, AES-CBC 사용<br><br>

- 비대칭키 방식<br>
  방식1 - 공개키로 암호화 / 개인키로 복호화<br>
  받는 사람이 공개키와 개인키를 생성<br>
  메세지를 받는 사람이 만든 공개키로 암호화하고 전송<br>
  암호화된 메세지를 받으면 받는 사람의 개인키로 복호화<br><br>

  방식2 - 개인키로 암호화 / 공개키로 복호화<br>
  보내는 사람이 공개키와 개인키를 생성<br>
  메세지를 보내는 사람의 개인키로 암호화하고 전송<br>
  암호화된 메세지를 받은 사람이 보낸 사람의 공개키로 복호화<br>

  해커가 공개키와 개인키를 모두 미리 위조하고 메세지를 변조하고 공개키로 암호화하면 기밀성 / 무결성 위험<br>
  거듭제곱과 큰 소수를 이용한 연산을 주로 이용하므로 계산 속도가 느리며 전자 상거래 및 인터넷 뱅킹에 사용된다<br>
  N개의 서로 다른 노드에 키를 분배하려면 2N개가 필요하다<br>
  예시: Diffie-Hellman / RSA<br><br>

    - RSA 비대칭키 방식 이해 - 단방향 암호화 방식 - 무결성을 검증할 때 사용한다<br>
      서버에서 두 개의 소수 p, q를 선택한다<br>
      파이n = (p - 1) * (q - 1)과 서로소인 공개키 kp를 결정한다<br>
      (kp * ks) mod 파이(n) = 1을 만족하는 개인키 ks를 결정한다<br>
      두 소수의 곱 N을 계산한다<br>
      kp와 N을 공개한다<br>
      암호화: 평문 P를 공개키 kp로 거듭제곱 한 후에 N으로 나눈 나머지로 암호화한다<br>
      복호화: 암호문 C를 개인키 ks로 거듭제곱 한 후에 N으로 나눈 나머지로 복호화한다<br>
      만약 N과 kp를 가지고 ks를 알아낼 수 있다면 암호가 깨지게 되지만 소수의 분해가 어렵기 때문에 이를 방지할 수 있다<br>
      만약을 위해 두 소수의 곱 N은 1024비트 길이를 사용한다<br><br>

    - Diffie-Hellman 비대칭키 방식 이해 - 양방향 암호화 방식 - 기밀성과 무결성이 모두 필요할 때 사용한다<br>
      데이터를 주고 받을 2개의 노드가 모두 공유하는 전역 변수인 소수 p와 p의 원시근 r을 선택한다<br>
      노드 a는 p보다 작은 비밀 양의 정수 a를 선택해서 r의 a제곱을 p로 나눈 나머지를 공개키 ya로 선택한다<br>
      노드 b도 마찬가지 방식으로 공개키 yb를 선택한다<br>
      이제 두 노드가 공개키를 교환한다<br>
      노드 a는 노드b의 공개키 yb를 자신의 비밀 양의 정수 a로 거듭제곱하고 p로 나눈 나머지를 자신의 비밀키 K로 결정한다<br>
      노드 b는 노드a의 공개키 ya를 자신의 비밀 양의 정수 b로 거듭제곱하고 p로 나눈 나머지를 자신의 비밀키 K로 결정한다<br>
      모듈러 연산의 특징에 의해 양쪽의 비밀키 K가 동일해진다<br>
      공개키로 비밀 정수를 알아내는 것이 대수적으로 불가능하다<br>
      문제는 애초에 처음부터 공개키를 교환하는 과정에서 해커가 관여하면 해커에 의한 서로 다른 비밀키 K1 K2가 생성된다<br>
      이를 위해 인증된 Diffie-Hellman 비대칭키 방식을 사용한다<br><br>

    - 인증된 Diffie-Hellman 비대칭키 방식 이해<br>
      애초에 처음에 공개키를 생성하고 전달할 때 무결성을 위해서 전자서명을 하고 상대에게 보낸다...어떻게...? 이제 나옴<br><br>


- 해쉬함수 - 인증<br>
  메시지를 일정 길이의 블록(예, 512비트)으로 분할 후 해쉬 함수에 입력☞짧고 일정한 길이의 메시지 다이제스트 생성)<br>
  예시: MD5, SHA-1<br>
  계산 효율이 좋아야 / 일방향성 / 강한 충돌 회피성<br>
  SHA: Secure Hash Algorithm / 뒤에 넘버링은 블럭 길이와 다이제스트 길이에 따라 다름<br><br>

    - 대칭키 암호 기반(DES)의 메시지 인증<br>
      보내고자 하는 메세지에 해쉬 함수를 적용해서 메세지 다이제스트를 만든다<br>
      사전에 교환되어 있는 대칭키 키로 메세지 다이제스트를 암호화해서 메세지 인증 코드를 생성한다<br>
      메세지와 인증코드를 전송한다<br>
      받는 사람은 받은 메세지에 해쉬함수를 적용해서 메세지 다이제스트를 만든다<br>
      받은 메세지 인증 코드를 사전에 교환되어 있던 대칭키로 복호화해서 메세지 다이제스트를 확인한다<br>
      두 메세지 다이제스트가 일치한다면 개인키가 안전했다는 가정 아래에<br>
        1. 메세지를 보낸 사람이 나와 같은 개인키를 가지고 있다는 무결성을 보장한다<br>
        2. 메세지가 중간에 변조되지 않았다는 무결성을 보장한다<br>
        3. 전체 메세지의 무결성을 해쉬 결과인 다이제스트 메세지에만 암호 알고리즘을 적용해서 속도가 빠르다<br><br>

    - 공개키 기반(RSA)의 메세지 인증<br>
      보내고자 하는 메세지에 해쉬 함수를 적용해서 메세지 다이제스트를 만든다<br>
      메세지를 보내는 사람의 개인키로 메세지 다이제스트를 암호화해서 메세지 인증 코드를 생성한다<br>
      메세지와 인증코드를 전송한다<br>
      받는 사람은 받은 메세지에 해쉬함수를 적용해서 메세지 다이제스트를 만든다<br>
      받은 메세지 인증 코드를 메세지를 보낸 사람의 공개키로 복호화해서 메세지 다이제스트를 확인한다<br>
      두 메세지 다이제스트가 일치한다면 공개키가 안전했다는 가정 아래에<br>
        1. 메세지를 보낸 사람이 내가 사용한 공개키를 만든 사람이라는 결성을 보장한다<br>
        2. 메세지가 중간에 변조되지 않았다는 무결성을 보장한다<br>
        3. 전체 메세지의 무결성을 해쉬 결과인 다이제스트 메세지에만 암호 알고리즘을 적용해서 속도가 빠르다<br><br>

    - 공유 비밀키 기반(Diffie-Hellman)의 메세지 인증 = HMAC(HMAC-MD5, HMAC-SHA-1은 IP 보안 프로토콜의 인증 기능에 사용되는필수 알고리즘)<br>
      비밀키를 사전에 공유 보내고자 하는 메세지에 비밀키를 포함시킨다
      (비밀키 + 메세지) 전체에 해쉬 함수를 적용해서 메세지 다이제스트를 만든다<br>
      비밀키를 제외한 메세지와 메세지 다이제스트를 전송한다<br>
      받는 사람은 받은 메세지에 사전 공유된 비밀키를 추가해서 해쉬함수를 적용하고 메세지 다이제스트를 만든다<br>
      만들어진 메세지 다이제스트가 받은 메세제 다이제스트와 일치하는지 확인한다<br>
      두 메세지 다이제스트가 일치한다면 사전 공유된 비밀키가 안전했다는 가정 아래에<br>
        1. 메세지를 보낸 사람이 내가 사용한 비밀키를 가진 사람이라는 무결성 보장한다<br>
        2. 메세지가 중간에 변조되지 않았다는 무결성을 보장한다<br>
        3. 전체 메세지의 무결성을 해쉬 결과인 다이제스트 메세지에만 암호 알고리즘을 적용해서 속도가 빠르다<br><br>

- 공개키 인프라 구조<br>
  공개키의 위조를 방지하기 위하여 자신의 공개키 및 개인 정보를 인증기관에 인증서로 등록<br>
  사용자: 인증서를 발행받아 사용<br>
  등록기관: 인증서 신청자의 신원 확인 및 인증서 등록을 대행하는 기관<br>
  인증기관: 인증서 발생하는 기관<br>
  저장소: 인증서 및 인증서 취소 목록 저장<br><br>

    - 인증서 = 개인의 정보 / 개인의 공개키 / 인증기관의 정보 / 인증기관의 개인키로 서명(예시: X.509, PKIX)<br>
      인증서가 진짜라는 것은 인증기관(CA; Certificate Authority)이 보증해준다<br>
      그 인증기관의 보증을 어떻게 신뢰하는가 - 계층적 신뢰 모델을 사용한다<br>
      최상위 인증기관의 개인키는 엄격한 보안이 요구<br>
      최소한 160비트 메시지 다이제스트를 갖는 해쉬함수 사용 / 개인키의 길이는 최소한 2048 비트 사용<br><br>

    - 키 생성 및 관리 : 사용자 키 생성 방식<br>
        1. 토큰 생성 : 인증기관에서 사용자의 신분확인, 사용자가 자신의 공개키/개인키 쌍을 생성할 수 있는 토큰을 발행<br>
        2. 토큰을 안전한 채널로 사용자에게 전송<br>
        3. 키 생성 : 공개키 개인키 생성<br>
        4. 인증서-생성 요청 : 사용자가 인증기관에 공개키를 포함하고 있는 인증서-생성 요청 메시지 전송<br>
        5. 인증서-생성 응답 : 인증서-생성 요청 메시지의 유효성을 확인 후, 응답 메시지 사용자에게 전송<br>
        6. 인증서 저장 : 발급한 인증서를 인증서 보관소에 저장<br><br>

    - 키 생성 및 관리 : 중앙 집중형 키 생성 방식<br>
        1. 토큰 생성 : 인증기관에서 사용자의 신원확인 후 토큰 생성, 토큰에는 인증기관이 생성한 사용자의 공개키/개인키 쌍과 인증서 포함<br>
        2. 토큰을 안전한 채널로 사용자에게 전송<br>
        3. 인증서 저장 : 인증기관에서 발급한 인증서를 인증서 보관소에 저장<br>
        4. 사용자는 토큰에 있는 인증서와 공개키/개인키 사용<br><br>

- 인터넷 보안 프로토콜<br>
  인터넷 초기에는 보안이 중요한 고려 요소가 아니어서 헤더 검사합 필드 정도만 있었는데 이는 충분히 조작 가능한 수준이었음<br><br>

  현재에는 크게 3가지 종류의 보안이 인터넷 환경에 적용된다<br>
  IPSec: 키관리(ISAKMP), 인증헤더(AH), 캡슐화 보안 페이로드(ESP) 및 압축 프로토콜<br>
  SSL(Secure Socket Layer): 웹 서버와 브라우저 사이의 안전한 통신을 위해 개발됨, 서버/클라이언트 인증, 기밀성 보장, HTTPS에 적용<br>
  TLS(Transport Layer Security): SSL 을 기반으로 표준화<br><br>

  - IPSec<br>
    인증 코드를 통한 IP 패킷의 무결성과 인증 기능을 제공 + 암호화를 통한 기밀성도 제공 + 재전송된 패킷의 감지 및 폐기
    네트워크 계층에서 적용되므로 트랜스포트레이어와 어플리케이션 레이어에서는 이미 보안이 보장된다
    기존의 IP 계층 바로 아래에 IPSec을 추가적으로 구현(IPV6은 인증헤더(인증)와 ESP헤더(암호화)를 삽입하는 방식으로 해결)
    1. 보안연계 (SA: Security Association)
       : IP 보안 프로토콜, 프로토콜의운용모드, 보안 알고리즘, 보안 키와 키의 수명 등에 대한 통신 쌍방 간의합의
       : 인증헤더(AH) 보안연계 / 캡슐화 보안 페이로드(ESP) 보안연계 / 압축(IPComp) 보안연계
       - 트랜스포트 모드
           - 호스트와 호스트 간의 보안 연계
           - 원래 IP 헤더의 발신지 및 목적지 주소를 그대로 유지
       - 터널 모드
           - 보안 게이트웨이와 보안 게이트웨이 사이 or 호스트와 보안 게이트웨이 사이
           - 보안 게이트웨이에서 IPSec 프로토콜 구현
           - 새로운 IP 헤더를 만들어 원래의 IP 패킷을 모두 페이로드화
       
       - 보안 정책 데이터베이스(SPD) :
           - IP 패킷의 선택자 정보를 이용하여 IP 패킷에 IPSec 적용 여부 판단
           - 패킷에 IPSec 을 적용하는 경우 보안 연계 데이터베이스의 관련 항목 지정
           - IPSec 적용 여부를 결정하기 위해 하나 이상의 선택자 정보를 이용
                - 발신지 및 목저지 IP 주소
                - 전송 계층 프로토콜 종류
                - etc...
           - 지시자 : 선택자들과 일치하는 IP 패킷의 폐기, 통과 또는 IPSec 처리를 지시
           - IPSec 처리가 요구되는 경우 보안 연계 데이터베이스의 관련 항목을 지정

        - 보안 연계 데이터베이스(SAD) :
         보안 연계와 관련된 암호 및 인증 알고리즘과 키 값 등의 매개변수 저장
       
       터널 모드
       적용 구간: 보안 게이트웨이와 보안 게이트웨이 사이 또는 호스트와 보안 게이트웨이 사이
       로컬 네트워크의 호스트들을 대신하여 보안 게이트웨이에 IPSec 프로토콜 구현l 새로운 IP 헤더를 만들어 원래의 IP 패킷을 모두 페이로드화 함
    
    2. ISAKMP 프로토콜: 보안연계의 설정 및 해제 기능 담당
      키 생성 / 분배 / 관리
    
    3. AH 및 ESP 프로토콜
      AH(인증 헤더) 프로토콜:  패킷의 근원에 대한 인증과 전송 중에 변조되지 않았음을 보장하는무결성 서비스 제공
      ESP(캡슐화 보안 페이로드) 프로토콜:  IP 패킷의 기밀성 제공을 위한 암호화 기능과 무결성및 인증 기능 제공
      인증 및 무결성 서비스: HMAC-MD5, HMAC-SHA-1
      기밀성 서비스: 3DES-CBC, AES-CBC
    
    4. IPComp 프로토콜: IP 보안 프로토콜의 사용으로 증가되는 IP 패킷의 길이를 감소시켜 대역폭 사용의 효율성을높임

    - SSL
    - Public Key로 암호화 하면 Data 보안
        - 상대방의 Public key로 data를 암호화 하고 전송하면, data를 수신한 사람은 자신의 Private key로 data를 복호화 한다.
        - 키로 암호화 한다면, B키로 복호화가 가능하고, B키로 암호화를 한다면 A키로 복호화가 가능한 것이다. Public Key는 널리 배포될 수 있기 때문에 많은 사람들이 한 명의 Private Key
          소유자에게 data를 보낼 수 있다.
    - Private Key로 암호화 하면 인증 과정에 중점을 둔다.
        - Private Key의 소유자가 Private Key로 data를 암호화하고 Public Key와 함께 전달한다.
        - 이 과정에서 Public Key와 data를 획득한 사람은 Public key를 이용하여 복호화가 가능하다. 이런 위험에도 불구하고 이 방법을 사용하는 이유는 data 보호의 목적 보다는 Public
          Key data 제공자의 신원을 보장해주기 때문이다. 암호화된 data가 Public Key로 복호화 된다는 것은 Public Key와 쌍을 이루는 Private Key에 의해서 암호화 되었다는 것을
          의미한다. 즉 data 제공자의 신원 확인이 보장된다는 것이다.
    
    3 way hand shaking 절차가 끝난 후 에플리케이션 레이어의 메세지가 https 프로토콜을 따르는 경우 추가적으로 SSL handshake 절차가 진행된다
    
    1. 클라이언트 브라우저 주소창에서 naver.com을 치면 내 브라우저는 네이버 웹 서버에 접속을 시도함 TCP연결을 위한 3-way handshake를 수행한 브라우저는 네이버가 HTTPS를 사용하는 것을 알게
       되고 다음의 정보를 보냄 브라우저가 사용하는 SSL 혹은 TLS 버전 정보 브라우저가 지원하는 암호화 방식 모음(안전한 키 교환, 전달 대상 인증, 암호화 알고리즘, 메세지 무결성 확인 알고리즘)
       브라우저가 순간적으로 생성한 임의의 난수 만약 이전에 SSL 핸드 셰이크가 완료된 상태라면, 그 때 생성된 세션 아이디 기타 확장 정보
    2. 서버 다음 정보를 클라이언트에 제공함. 브라우저의 암호화 방식 정보 중에서, 서버가 지원하고 선택한 암호화 방식 서버의 공개키가 담긴 SSL 인증서 서버가 순간적으로 생성한 임의의 난수 클라이언트 인증서
       요청 (선택 사항)
    3. 클라이언트 브라우저는 서버의 SSL 인증서가 믿을만한지 확인함 등록된 CA가 아니거나, 등록된 CA가 만든 인증서처럼 꾸몄다면 경고 브라우저는 자신이 생성한 난수와 서버의 난수를 사용하여 premaster
       secret을 만듬 웹 서버 인증서에 딸려온 웹 사이트의 공개키로 암호화하여 서버로 전송함
    4. 서버 서버는 사이트의 비밀키로 브라우저가 보낸 premaster secret값을 복호화 복호화한 값을 master secret 값으로 저장 이것을 사용해서 방금 브라우저가 만들어진 연결에 고유한 값을 부여하기
       위한 session key를 생성 이 세션 키를 대칭키 암호화에 사용해서 브라우저와 서버 사이에 주고받는 데이터를 암호화하고 복호화함
    5. HTTPS 통신을 시작함: 세션 키를 사용하여 암호화/복호화하며 HTTPS 프로토콜을 통해 주고받을 수 있음
    6. 공개키와 비밀키를 복합해서 쓰는 이유 공개키 방식은 암/복호화 과정에서 많은 컴퓨터 파워를 사용하기 때문 만약 공개키를 그대로 사용하면 많은 접속이 몰리는 서버는 매우 큰 비용을 지불해야 함 반대로 대칭키는
       암호를 푸는 열쇠를 상대에게 전송해야 하는데 이걸 그냥 전송하면 위험함
    7. 그래서 속도는 느리지만 데이터를 안전하게 주고 받을 수 있는 공개키 방식으로 대칭키를 암호화하고 실제 데이터를 주고 받을 때는 대칭키를 이용해서 데이터를 주고 받음