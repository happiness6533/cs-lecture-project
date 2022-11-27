# 1. 프로그래밍의 3대 요소
# 데이터: 프로그래밍은 데이터를 다루는 일이다
# 함수: 데이터를 다루는 일이 반복된다면 함수로 만들어서 어디에서나 쓰도록 한다
# 논리: 조건문과 반복문으로 논리를 코드로 표현한다

# 2.
# 코멘트 자료형(문자 숫자 불린) 변수 콘솔 gui 프린트 포멧팅 형변환 연산자(= == != 사칙연산)
name = "하하맨"
birth = 2000
now = 2021

# 3.
# 사전 배열 튜플 집합

# 사전: 조회
user1 = {"name": "하하맨", "birth": 2001}
user2 = {"name": "하하걸", "birth": 2002}
user3 = {"name": "호호맨", "birth": 2003}
user4 = {"name": "호호걸", "birth": 2004}
user5 = {"name": "후후맨", "birth": 2005}

# 배열: 조회, 변경, 추가, 삭제
users_array = [user1, user2, user3, user4, user5]
a, b, c, d, e = users_array

# 튜플: 조회 가능, 변경, 추가, 삭제 불가
numbers_tup = tuple(range(5))
users_tuple = (user1, user2, user3, user4, user5)

# 셋: 원소의 순서가 정해져 있지 않으며, 중복 불가능하고, 조회 불가, 집합 연산 가능
a_set = {1, 2, 3, 4, 4, 4}
b_set = {3, 4, 5, 6, 6, 6}


# 4. 함수 리턴
def get_age(now, birth):
    return now - birth + 1


# 1. 파이썬 함수의 로컬 변수는
#     - 정의되지 않은 로컬 변수에 접근하려는 경우, 상위 스코프에서 찾아보고, 발견하면 변수를 읽을 수 있다 / 쓸 수는 없다
#     - global 변수로 정의하고 접근하려는 경우, global 스코프에서 찾아보고, 발견하면 변수를 읽을 수 있다 / 쓸 수도 있다
#     - 위의 두 경우 모두 비순수함수를 작성하게 되기 때문에 바람직하지 않고, 가능하면 순수함수로 작성한다
#
# 2. 순수함수로 작성한 경우 파이썬의 함수는 call by assignment로 작동한다
#     - 왜냐하면 파이썬의 모든 자료형은 객체이며(정수와 같은 값도 Integer와 같은 wrapper 클래스로 객체화 되어있다)
#     - b = a의 경우 a가 불변형이라면(ex: 정수) b에는 새로운 주소값을 가지는 객체가 할당되고
#     - b = a의 경우 a가 불편형이 아니라면(ex: 리스트) b는 a와 같은 객체를 가리키기 때문에
#     - 함수의 argument에 parameter가 할당되는 순간에 불변형과 비불변형에 따라 로컬 변수가 다르게 이해된다
#     - 우선, argument에 불변형 parameter를 할당하는 경우, 새로운 주소값을 가지는 새로운 객체가 함수 내부의 로컬 변수로 생성된다
#     - 즉, call by value처럼 외부 스코프에 영향을 주지 않는다
#     - 그러나, argument에 비불변형 parameter를 할당하는 경우, 기존의 객체가 함수 내부의 로컬 변수로 사용된다
#     - 즉, call by reference처럼 외부 스코프에 영향을 준다
#     - 이렇게 parameter에 따라 함수 내부의 로컬 변수가 다르게 이해되는 작동 방식을 call by assignment라고 한다
#
# 3. 그래서 결국 파이썬의 함수는 어떻게 사용하는 것이 바람직한가?
#     - 순수 함수로 작성하라
#     - 만약 함수의 parameter에 불변형 자료를 사용하는 경우, 그리고 그 값을 함수 내부에서 읽기만 하는 경우, 고민하지 않는다
#     - 만약 함수의 parameter에 불변형 자료를 사용하는 경우, 그리고 그 값을 함수 내부에서 다시 쓰는 경우, 반드시 리턴을 사용해서 외부에 반영한다
#     - 만약 함수의 parameter에 비불변형 자료를 사용하는 경우, 그 값을 함수 내부에서 읽기만 하는 경우, 고민하지 않는다
#     - 만약 함수의 parameter에 비불변형 자료를 사용하는 경우, 그 값을 함수 내부에서 다시 쓰는 경우, 어차피 외부에 반영되므로, 고민하지 않는다
# 함수 사용시 주의사항(전역 = 현실 / 함수 = 꿈)

# 절차 지향적으로 프로그래밍 하는 경우 case 1 = 현실에서 현실을 바꾸면 당연히 바뀐다
# x = 10
# x = x + 1
# print(x)

# 절차 지향적으로 프로그래밍 하는 경우 case 2 = (꿈에서 결과를 얻은 후) 현실에서 현실을 바꾸면 당연히 바뀐다
# 전역 상태와 무관하게 받은 파라미터만 활용해서 연산하는 함수 = 순수함수
# => 순수함수로 값을 리턴 후 전역 변수에 재대입 => 파이썬 추천(메모리 문제 발생 => GC가 처리한다)
# x = 10
# def add_one(input):  # 전역 상태와 무관하게 받은 파라미터만 활용해서 연산하는 함수 = 순수함수
#     input = input + 1
#     return input
# x = add_one(x)
# print(x)

# 절차 지향적으로 프로그래밍 하는 경우 case 3 = 꿈에서 현실을 바꾸는 경우
# => 함수 내부에서 global 키워드를 쓴다 => 비추천
# x = 10
# def add_one():
#     global x
#     x = x + 1
# add_one()
# print(x)

# 절차 지향적으로 프로그래밍 하는 경우 case 4 = 꿈에서 현실을 바꾸는 경우
# call by address(kind of call by value) => c++ 가능, 비추천
# call by reference => c++ 가능, 추천(메모리 이익)

# x = 10
# def add_one(input_ptr):  # call by address(kind of call by value)
#     *input_ptr = *input_ptr + 1
# add_one(*x)
# print(x)

# x = 10
# def add_one(&input):  # call by reference
#     input = input + 1
# add_one(x)
# print(x)

# 객체 지향적으로 프로그래밍을 하는 경우
# => 순수함수로 값을 리턴 후 전역 변수에 재대입 방법 대신
# => 파이썬, c++ 모두 인스턴스 변수를 변경하는 것을 권장

# 함수의 다양한 사용법
# 함수에 전달할 파라미터가 기본값을 가지게 하고 싶은 경우: 인자의 제일 마지막 부분에 파라미터를 두고 초기값을 지정
# 함수에 전달할 파라미터의 개수가 가변적인 경우: 언패킹 방식으로 전달 = 함수(*리스트) 함수(*튜플) 함수(**딕셔너리)
# 함수를 블록처럼 활용해서 기능을 확장하고 싶다면: 데코레이터
def add_one(a, b=1):
    print(a + b)


def print_numbers(a, *args):
    print(a)
    for arg in args:
        print(arg)


# 이 방식으로 오버로딩 구현
def func(*args):
    if len(args) == 1:
        print(args)
    else:
        print("!!!")
        print(args)


func(1)
func(1, 2)


def personal_info(**kwargs):
    if "name" in kwargs:
        print("이름: ", kwargs['name'])
    if "age" in kwargs:
        print("나이: ", kwargs['age'])
    if "address" in kwargs:
        print("주소: ", kwargs['address'])


def myDecorator(original):
    def expanded_function(n):
        return 2 * original(2 * n)

    return expanded_function


@myDecorator
def add_one_function(n):
    return n + 1


# 필요한 순간에 함수를 잠시 만들어서 사용하고 사라지게 만들어서 메모리 공간의 낭비를 줄이고 싶다면: 익명함수 람다를 사용
temp_function = lambda now, birth: now - birth + 1 if birth > 0 else 0

if __name__ == "__main__":
    print(f"내 이름은 {name}입니다.")
    print(user1["name"])
    print(a, b, c, d, e)
    print(numbers_tup[0])
    print(a_set)
    print(b_set)
    print(a_set | b_set)
    print(a_set & b_set)
    print(a_set - b_set)
    print(a_set ^ b_set)
    print(f"내 나이는 {get_age(now, birth)}살 입니다.")

    # 5. if elif else switch

    # 6. while + flag  / while + break / for
    i = 0
    while i < len(users_array):
        print(f"나는 {users_array[i]['name']}입니다. 내 나이는 {get_age(now, users_array[i]['birth'])}살 입니다.")
        i = i + 1

    i = 0
    while True:
        print(f"나는 {users_array[i]['name']}입니다. 내 나이는 {get_age(now, users_array[i]['birth'])}살 입니다.")
        i = i + 1
        if i == len(users_array):
            break

    for i in range(len(users_array)):
        print(f"나는 {users_array[i]['name']}입니다. 내 나이는 {get_age(now, users_array[i]['birth'])}살 입니다.")
