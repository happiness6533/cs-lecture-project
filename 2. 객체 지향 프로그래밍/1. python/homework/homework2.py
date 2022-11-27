# 연습2: 연습 1의 기능을 보강하자
# 유저의 정보를 인풋으로 입력을 받아서
# 선택된 유저의 정보를 파일에 쓰자
# 파일을 읽고 배열에 담아주자
# 인풋이 잘못된 경우 프로그램을 종료하지 않고 입력일 잘못되었다고 처리를 해주자

def sign_up():
    input("name:")
    input("age")

def log_in():
    pass

if __name__ == "__main__":
    me = None
    while True:
        try:
            if me is None:
                choice = input("0 or 1")
                if choice == 0:
                    sign_up()
                else:
                    log_in()
            else:
                print(f"{me} is enter")
                input("단어장 준비")
                # 단어장 오픈
        except Exception as e:
            print(e)
