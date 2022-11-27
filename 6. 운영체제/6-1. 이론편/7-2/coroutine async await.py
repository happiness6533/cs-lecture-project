# 싱글쓰레드 논블로킹 코드 흐름 이해하기
# 핵심 키워드: 제너레이터, 코루틴, 퓨쳐, 태스크, 런루프(이벤트 루프)


####################################################################################################
# 1. 제너레이터 함수
####################################################################################################
# 제러레이터 함수는 제너레이터 객체를 반환하는 함수다
# 제너레이터 객체는 일종의 이터레이터 객체이다

# caller 함수는 제네레이터 함수를 호출하여 제네레이터 객체를 얻고
# next(gen)으로 제네레이터 함수 내부를 실행한다
# 실행 도중에 yield 키워드를 마주치게 되면
# 제너레이터 함수는 자신의 실행과 관련된 상태(스택, 실행 위치 등)를 프로세스의 스택과 힙 사이 어딘가에 저장한 뒤 실행을 중단하고
# caller 함수에게 제어권을 양보하면서 yield 키워드의 뒤에 오는 값을 리턴으로 넘겨준다

# 제어권을 다시 넘겨받은 caller 함수가 다시 동일한 방법으로 해당 제네레이터를 실행하면
# 실행이 중단되었던 부분부터 다시 실행을 시작하게 되고
# 또 다시 yield 키워드를 마주치면 위와 동일한 행동을 반복한다

# 만약 yield 키워드를 모두 소모한 제네레이터를 실행하는 경우 StopIteration 예외가 발생한다
####################################################################################################


####################################################################################################
# 2. 코루틴
####################################################################################################
# 코루틴을 호출하면 코루틴 객체가 반환된다
# 코루틴 객체는 제너레이터 객체에 한 가지 기능이 추가된 함수이다
# 추가된 한 가지 기능이란, 값을 메인 루틴에서 코루틴으로 전달하는 것을 말한다

# 만약 caller 함수가 코루틴 객체의 send(값) 메소드를 호출하면
# 실행이 중단되었던 부분에 위치한 yield 키워드 구문의 자리를 send(값)의 값이 대체한다

# 정리하자면
# 코루틴 내부에서: yield 값 = 코루틴이 caller에게 값을 넘겨주는 것
# 메인루틴에서 co.send(값) = 코루틴 내부로 값을 전달하는 것

# 코루틴을 간단하게 만드는 방법으로 함수의 앞에 async 키워드까지 붙일 수 있다
####################################################################################################


####################################################################################################
# 3. 중첩 제네레이터
####################################################################################################
# 아래의 예시처럼 제네레이터가 내부에서 또 다른 제네레이터를 실행하는 것이 가능하다
def generator1():
    yield 1
    yield 2
    yield 3


def generator2():
    go1 = generator1()
    for element in go1:
        yield element


# 위의 예시를 더 간단하게 표현할 수 있다
def generator3():
    go1 = generator1()
    yield from go1


print(generator3().__next__())

# yield from 키워드의 뒤에는 제네레이터 객체뿐 아니라 __iter__() 메소드가 구현된 이터러블 객체라면 올 수 있다

# 위 코드의 흐름은 다음과 같다
# : 제너레이터3가 yield from을 만나 제너레이터1 객체를 실행한다
# : 제너레이터3가 제너레이터1으로 제어권을 넘겨준다
# : 제너레이터1이 yield를 만나서 값 1을 yield하고 제어권을 제너레이터3 에게 돌려준다
# : 값 1을 받은 제너레이터3가 1을 yield하고 메인 루틴으로 제어권을 넘겨준다
# : 메인 루틴은 값 1을 출력한다
####################################################################################################


####################################################################################################
# 4. 코루틴의 중첩
####################################################################################################
# 제너레이터와 사용법이 동일하다
# 코루틴이 내부에서 또 다른 코루틴을 실행하는 것이 가능하다
####################################################################################################


####################################################################################################
# 5. 발전된 문법
####################################################################################################
# 코루틴 함수를 정의하려면 함수의 앞에 async를 붙이면 된다
# yield from 대신 await를 쓸 수 있다
# await 키워드의 뒤에는 코루틴 객체뿐만 아니라 __await__() 메소드가 구현된 Awaitable 객체라면 무엇이든지 올 수 있다
####################################################################################################


####################################################################################################
# 6. 퓨처 객체와 태스크 객체(await 키워드의 뒤에 올 수 있는 Awaitable 객체이다)
####################################################################################################
# 6-1. 퓨처 객체
# 퓨처 객체는 io와 같은 작업의 실행 상태 및 결과를 저장해서 객체 외부에서 결과를 확인하기 쉽게 하려고 설계된 객체이다

# 퓨쳐 객체의 중요한 데이터
# 실행 상태란 해당 작업이 진행 중인지, 취소되었는지, 종료되었는지를 말한다
# 퓨처 객체는 PENDING, CANCELLED, FINISHED의 세 가지 상태 중 하나를 내부 데이터로 가진다

# 퓨쳐 객체의 중요한 메소드
# 퓨처 객체의 중요한 메소드 중 하나는 add_done_callback()이다
# 이 메소드를 호출하면 해당 퓨처 객체가 완료(Done)될 때 호출될 함수를 등록할 수 있다


# 6-2. 태스크 객체(자바스크립트의 프로미스와 거의 동일한 객체이다)
# 태스크는 퓨처의 자식 객체이다

# 태스크 객체를 생성하려면
# asyncio.run(코루틴 객체), asyncio.create_task(코루틴 객체) 함수를 호출하면 된다
# 태스크 객체가 생성될 때 넘겨받은 코루틴 객체는 내부의 _coro 필드에 저장한다

# 태스크 객체의 중요한 데이터
# _coro = 외부에서 받은 코루틴 객체

# 태스크 객체의 중요한 메소드
# def __step():
# 자신이 가지고 있는 코루틴 객체를 실행하는 메소드이다

# 코루틴 객체가 생성되면 코루틴 객체는 현재의 이벤트 루프에게 자신의 __step() 메소드를 호출해줄 것을 요청한다
# 이것을 보고 코루틴이 태스크로서 실행되도록 이벤트 루프에 예약을 건다라고 표현한다

# 잠시 후에 이벤트 루프에 의해서
# 예약된 태스크 객체의 __step() 메소드가 호출되고
# 태스크 객체 내부의 코루틴이 실행된다
# 그렇게 처음 실행된 코루틴은 await 키워드를 이용하여 또 다른 코루틴을 부를 수 있고 그 코루틴은 또다시 다른 코루틴을 부를 수 있다
# 이러한 스레드의 실행 흐름을 코루틴 체인이라고 부른다
# 이처럼 하나의 태스크 객체는 현재의 태스크에 속하는 코루틴 체인의 실행을 관리하는 역할을 맡는다

# 코루틴 체인을 흘러가다 보면 언젠가 sleep 혹은 io 관련 코루틴을 await 하는 코드를 만난다
# 태스크 객체는 이러한 상황이 되면 실행을 중단하고 이벤트 루프에게 제어권을 넘겨준다
# 그러고 나면 이벤트 루프는 자신에게 실행을 예약해둔 태스크들 중 우선순위가 높은 것을 적절히 선택하여 실행시키며

# 시간이 흘러 아까 실행이 중단되었던 태스크가 다시 재실행을 이어갈 수 있는 상태가 되면
# 해당 태스크는 다시 이벤트 루프에게 자신의 재실행을 예약한다
# 그러면 언젠가 이벤트 루프에 의해 다시 순서가 돌아와서 쓰레드가 해당 태스크를 재실행할 수 있게 될 것이다

# 한편, 태스크 객체가 자신이 가진 해당 코루틴이 모든 yield 키워드를 소진해서 StopIteration 예외가 발생하면
# 그 객체로부터 반환 값을 얻어서 자기 자신(태스크 객체)의 결과 값을 업데이트한다
# 이는 해당 태스크의 실행이 완료된 상황을 의미하게 되어서 더 이상 이벤트 루프에 의해 실행이 예약될 수 없게 된다
# asyncio.run() 함수가 실행되는 것은 이로 인해 실행된 태스크의 실행이 완료될 때까지를 의미하는 것이다
####################################################################################################


####################################################################################################
# 6. 이벤트 루프
####################################################################################################
# 코루틴을 실행시키는 방법은
# 1. await 코루틴 객체
# 2. asyncio.run(코루틴 객체)
# 3. asyncio.create_task(코루틴 객체)

# 이 중에서 await 키워드는 코루틴 내에서만 사용할 수 있기 때문에
# 맨 처음 코루틴을 실행하는 용도로는 사용할 수 없다
# 최초에 한 번 코루틴이 실행되고 나면, 그 코루틴부터 시작해서 await 키워드를 이용하여 다른 코루틴을 호출할 수는 있다

# 그렇다면 남은 건 2번과 3번
# 이들은 코루틴 바깥에서 처음으로 코루틴을 실행할 수 있는, 즉 코루틴 체인으로 들어가는 일종의 엔트리 포인트이다.

# asyncio.run() 함수는 현재의 쓰레드에 새 이벤트 루프를 설정하고
# 해당 이벤트 루프에서 인자로 넘어오는 코루틴 객체에 해당하는 코루틴을 태스크로 예약하여 실행시킨 뒤
# 해당 태스크의 실행이 완료되면 이벤트 루프를 닫는 역할을 수행한다
# 3.7 버전 이상의 Python에서만 사용할 수 있기 때문에
# 그 이전 버전에서는 다음과 같이 코드를 작성해야 한다

# loop = asyncio.get_event_loop()
# loop.run_until_complete(first_coroutine())
# loop.close()

# loop = asyncio.get_event_loop()
# 이는 현재 쓰레드에 설정된 이벤트 루프를 가져오는 함수이다
# 그러나 만약 현재 쓰레드에 설정되어 있는 이벤트 루프가 없다면
# 이벤트 루프를 새로 생성하여 이를 현재 쓰레드에 설정한 뒤 해당 이벤트 루프를 반환한다
# 즉, 이 함수의 호출은 코루틴의 실행을 위해 이벤트 루프를 준비하는 과정으로 볼 수 있다

# 그런데 이벤트 루프가 정확히 무엇일까?
# 이벤트 루프란, 무한 루프를 돌며 매 루프마다 작업(= 태스크)을 하나씩 실행시키는 로직을 의미한다
# 따라서 위에서 언급했던, 현재 쓰레드에 이벤트 루프를 설정한다 함은
# 단순히 '이벤트 루프라는 로직을 실행시킬 수 있는 객체를 생성한 것' 정도로 이해하면 된다
# 이벤트 루프 객체를 이용하여 실제로 이벤트 루프를 실행시키는 것은
# 아래에서 설명할 run_until_complete() 메소드를 호출하는 순간부터이다.

# 그리고 여기서 말하는 작업이라는 것은 곧 앞서 소개했던 태스크 객체에 대응하는 태스크(Task)이다
# 태스크라는 것은 하나의 코루틴에서부터 출발하는 하나의 실행 흐름으로 볼 수 있다

# loop.run_until_complete(first_coroutine())

# 앞서 생성한 이벤트 루프 객체를 이용하여 실제로 이벤트 루프를 실행시키는 함수이다.
# 태스크의 실행 (코루틴 체인의 형성)
# 인자로 넘어오는 코루틴 객체를 이용하여 태스크 객체를 생성하고
# 그 과정에서 해당 태스크 객체가 나타내는 태스크의 실행이 이벤트 루프에 의해 즉시 예약된다
# 처음에는 실행이 예약된 다른 태스크가 없기 때문에
# 이벤트 루프는 이 태스크를 바로 실행할 것이다
# 이때 태스크의 실행이란, 해당 태스크 객체의 __step() 메소드를 호출하는 것을 의미한다
# 이 메소드는 코루틴 객체(_coro 필드에 저장되어 있음)의 send() 메소드를 호출함으로써
# 해당 코루틴을 실행하는 역할을 수행한다
# 그러면 이 코루틴을 시작으로 await 키워드를 마주칠 때마다 연쇄적으로 코루틴을 호출하며 코루틴 체인을 형성하게 될 것이다

# 코루틴 체인의 종착점 (await {Sleep 또는 I/O 관련 코루틴 객체})
# await 키워드를 통해 코루틴 체인을 형성하며 코루틴을 실행하다 보면
# 언젠가 Sleep 혹은 I/O 관련 코루틴(EX. asyncio.sleep() 등)을 await 하는 코드를 마주치게 될 것이다
# 그런데 이러한 종류의 코루틴들은 퓨처 객체를 await 하도록 구현되어 있다.

# 예를 들어 I/O 관련 코루틴이라고 해보자
# 그러면 이 코루틴은 특정 소켓에 대해 데이터를 읽거나 쓰기 위해 해당 소켓의 상태를 검사한다
# 만약 당장 읽거나 쓸 수 있는 데이터가 있다면
# 단순히 yield 키워드만을 사용하여 태스크 객체의 __step() 메소드로까지 제어를 넘긴다
# 그러면 태스크 객체는 바로 다시 자신의 실행을 이벤트 루프에게 예약하고 지금의 실행은 중단한 뒤
# 이벤트 루프에게 제어를 넘긴다
# 이 때 태스크의 실행을 예약한다 함은
# 해당 태스크 객체의 __step() 메소드를 이벤트 루프의 콜백 큐에 등록하는 것을 의미한다

# 그러나 보통은 당장 읽거나 쓸 수 있는 데이터가 있지 않다
# 따라서 보통의 경우에는 select() 함수를 이용하여 해당 소켓을 등록해두고
# 해당 소켓에 바인딩된 퓨처 객체를 새로 생성하여 await 한다
# 퓨처 객체의 __await__() 메소드는
# 자기 자신(퓨처 객체)을 yield 하도록 구현되어 있기 때문에
# 이로 인해 해당 퓨처 객체는 코루틴 체인을 다시 역으로 거슬러서
# 태스크 객체의 __step() 메소드로까지 리턴되어 전달될 것이다
# 참고로 select() 함수는
# : Unix의 select() 함수를 래핑 한 Python 함수로
# : 특정 소켓들에 대해 데이터를 읽거나 쓸 준비가 될 때까지 (원하는 시간만큼) 기다릴 수 있게 하는
# : Blocking 함수이다. 이는 (원하는 시간만큼) 기다린 후 데이터를 읽거나 쓸 준비가 된 소켓들을 반환한다.

# io가 아닌 Sleep 관련 코루틴의 경우, 이벤트 루프 자체의 타이머를 이용한다
# 만약 asyncio.sleep(1)이라면
# 이 코루틴은 퓨처 객체를 하나 생성한 뒤
# 이벤트 루프에게는 1초 뒤에 해당 퓨처 객체의 결과 값을 업데이트하도록 요청한다
# 그리고 그 퓨처 객체를 await 한다
# 그러면 마찬가지로 해당 퓨처 객체가 코루틴 체인을 따라 태스크 객체의 __step() 메소드로까지 전달될 것이다
# 그렇다면 이제 그렇게 전달된 퓨처 객체를 태스크 객체가 어떻게 처리하는지 알아보자.

# 태스크 객체의 퓨처 객체 처리
# 태스크 객체는 yield 된 퓨처 객체를 받으면
# 우선 이것을 자신의 __fut_waiter 필드에 저장한다(바인딩한다)
# 그리고 퓨처 객체의 add_done_callback() 메소드를 호출하여
# 해당 퓨처 객체가 완료 상태가 될 때 이벤트 루프에게 실행을 예약할 콜백 함수를 등록한다
# 이때 등록하는 함수는 곧 자기 자신의 __step() 메소드라고 생각해도 된다
# 이러한 콜백 함수의 실행을 이벤트 루프에게 예약한다는 것은 곧 해당 태스크의 실행을 예약한다는 것과 같은 말이다.

# 그러고 나면 이제 태스크 객체는 자신의 실행을 중단하고 제어를 이벤트 루프에게 넘긴다
# 그렇게 제어가 넘어가고 나면, 이벤트 루프는 다시 자신에게 실행을 예약해둔 태스크(정확히는 콜백 함수)들 중
# 우선순위가 높은 것을 적절히 선택하여 이를 실행시킨다
# 이벤트 루프는 이러한 과정을 반복하며 여러 태스크들을 동시적으로 실행하는 역할을 맡는다.

# 이벤트 루프의 Polling (I/O 소켓 검사)
# 그런데 만약 더 이상 자신에게 실행을 예약해둔 태스크가 없게 되면
# 이벤트 루프는 그 시간을 낭비하지 않고
# select() 함수를 이용하여 데이터를 읽거나 쓸 준비가 된 소켓을 계속 찾는다
# 만약 데이터를 읽거나 쓸 준비가 된 소켓을 찾게 되면
# 그 소켓에 바인딩되어 있는 퓨처 객체의 결과 값을 업데이트해주고
# 이로 인해 이 순간 아까 등록해두었던 콜백 함수의 실행이 이벤트 루프에서 예약될 것이다
# 콜백 함수의 실행을 예약한다는 건 곧 해당 태스크의 실행을 예약한다는 말이다.

# 태스크 객체의 실행 재개 (__step() 메소드 재실행)
# 그러면 이벤트 루프가 실행이 예약된 태스크를 실제로 실행시키는 과정을 한 번 살펴보자
# 태스크의 실행이란 곧 해당 태스크 객체의 __step() 메소드가 호출되는 것을 의미한다
# 이 메소드는 먼저 자기 자신(태스크 객체)과 퓨처 객체의 바인딩을 해제함으로
# 더 이상 기다리는 퓨처 객체가 없음을 나타내도록 하고
# 다시 자신의 코루틴 객체에 대해 send() 메소드를 호출함으로써 해당 코루틴의 실행을 재개하게 된다
# 그러면 다시 해당 퓨처 객체의 __await()__ 메소드에서 자기 자신을 yield 하는 부분까지 가게 된다.
# __await()__ 메소드로까지 돌아왔을 때
# 만약 I/O 관련 코루틴 때문에 기다리고 있었던 거라면
# 이제는 해당 소켓에 대해 데이터를 읽거나 쓸 준비가 되었다는 것이므로
# 해당 소켓(자기 자신에 바인딩되어 있음)에 대해 데이터를 읽거나 쓴 다음
# 그 값을 return 할 것이다
# 반면에 Sleep 관련 코루틴 때문이었다면 바로 return 할 것이다.

# 최초 코루틴의 Return (태스크 실행의 종료)
# 이러한 과정을 반복하다 보면 언젠가 태스크가 실행한 최초의 코루틴이 return 해야 하는 시점에 도달할 것이고
# 이로 인해 해당 태스크 객체의 __step() 메소드에선 StopIteration 예외가 발생할 것이다
# 그러면 태스크 객체는 그 예외 객체의 value 필드 값으로 자기 자신의 결과 값을 업데이트하고
# 자신의 실행을 종료한다
# 그러면 이 태스크는 더 이상 이벤트 루프에 의해 실행이 예약되지 않고 버려진다
# loop.run_until_complete() 함수의 실행이 끝나는 시점이 이때이다
# 그 태스크 객체의 결과 값이 곧 loop.run_until_complete() 함수의 반환 값이다.

# loop.close()
# loop.run_until_complete() 함수의 실행이 끝났다는 것은 이제 해당 이벤트 루프가 실행되지 않는다는 것이다
# 따라서 이벤트 루프를 닫아줘야 하는데, 이 역할을 수행하는 것이 loop.close() 함수이다

# 이벤트 루프의 실행 흐름 및 동작 원리
# 태스크 동시 실행 : asyncio.create_task() 함수
# 위에서 이벤트 루프가 태스크들을 동시적으로(Concurrent, not Parallel) 실행한다고 설명하였다
# 그런데 사실 asyncio.run() 함수는 기본적으로 하나의 태스크만을 생성하여 실행한다
# 따라서 코루틴 체인 과정에서 추가적인 태스크를 생성하여 실행하지 않았다면
# 현재의 태스크가 중단되었을 때 이벤트 루프는 실행시킬 다른 태스크가 없게 된다
# 태스크가 한 개라면 동시적인(Concurrent) 실행을 하는 것이 애초에 말이 되지 않는 것이다.

# 따라서 동시적인(Concurrent) 실행을 위해서는
# asyncio.create_task() 함수를 호출함으로써 태스크를 추가로 생성하여 실행해야 한다
# 이 함수를 호출할 때 코루틴 객체를 인자로 넘기면
# 해당 코루틴 객체를 이용하여 태스크 객체를 생성하고 이를 반환한다
# 그리고 앞서 말했듯 태스크 객체가 생성되면 해당 태스크 객체가 나타내는 태스크의 실행이
# 이벤트 루프에 의해 즉시 예약된다(즉시 실행이 아니다)
# 단, 이 함수는 3.7 버전 이상의 Python에서만 사용할 수 있기 때문에
# 그 이전 버전에서는 asyncio.ensure_future() 함수를 대신 사용해야 한다.

# 다음으로, 모든 퓨처 객체(태스크 객체 포함)들이 완료 상태가 될 때까지 기다리는 함수가
# asyncio.gather()이다
# 이 함수는 인자로 여러 개의 Awaitable 객체들을 받을 수 있는데
# 만약 코루틴 객체를 받으면 이는 자동으로 태스크 객체로 래핑이 된다
# 따라서 사실상 퓨처 객체(태스크 객체 포함)만 넘어간다고 생각해도 된다
# 그리고 모든 퓨처 객체들이 완료 상태가 되면 그것들의 결과 값들을 리스트 형태로 반환한다
# 그 순서는 인자로 넘긴 순서와 동일하다. 이 함수는 await 키워드의 뒤에서 호출될 수 있는 코루틴의 일종이다.
####################################################################################################


####################################################################################################
# 기타
# 동기 함수를 코루틴처럼 쓰기: loop.run_in_executor()

# 파이썬 대부분의 함수는 블로킹 방식으로 동작한다
# 예를 들어 requests 라이브러리가 제공하는 requests.get(), requests.post() 등의 함수는 블로킹 방식으로 작동하는 함수이다
# 어떻게 하면 이를 논블로킹 방식으로 작동하게 만들 수 있을까?

# 옵션1
# : 논블로킹 방식으로 다시 만들어진 모듈을 다운받는다

# 옵션2
# : loop.run_in_executor()를 사용한다
# : 이 함수는 논블로킹 방식의 함수를 별도의 쓰레드에서 실행시킨다
# : 마치 sleep 혹은 io 관련 작업을 별도의 쓰레드가 자신이 타이머 또는 io 장치인 척 하고 실행해 주는 것이다
####################################################################################################
import asyncio


async def get_pizza():
    print("피자 주세요")
    await asyncio.sleep(10)
    print("피자 서빙")


async def get_bread():
    print("빵 주세요")
    await asyncio.sleep(5)
    print("빵 서빙")


async def get_water():
    print("물 주세요")
    await asyncio.sleep(0)
    print("물 서빙")


async def server():
    tasks = [asyncio.create_task(get_pizza()),
             asyncio.create_task(get_bread()),
             asyncio.create_task(get_water())]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    # 제러레이터 예제
    # 코루틴 예제

    # 싱글쓰레드 논블로킹 예제
    loop = asyncio.get_event_loop()
    co = server()
    loop.run_until_complete(co)
