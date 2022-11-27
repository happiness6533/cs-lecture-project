from user import Influencer, Company


def sign_up():
    user_id = input("아이디를 입력하세요: ")
    user_password = input("비밀번호를 입력하세요: ")
    user_nick_name = input("닉네임을 입력하세요: ")
    user_type = input("사용자의 소속을 선택하세요. 일반 유저(0) vs 회사(1): ")

    user_file_writer = open("users.txt", "a", encoding="UTF8")
    user_file_writer.write(user_id + " " + user_password + " " + user_nick_name + " " + user_type + "\n")
    user_file_writer.close()


def log_in():
    user_id = input("아이디를 입력하세요: ")
    user_password = input("비밀번호를 입력하세요: ")

    me = None

    user_file_reader = open("users.txt", "r", encoding="utf8")
    while True:
        user_data = user_file_reader.readline()
        if user_data == '':
            break

        user_data = user_data.strip().split(" ")
        if user_id != user_data[0]:
            continue
        else:
            if user_password != user_data[1]:
                continue
            else:
                # 인플루언서인지 컴퍼니인지 구분해서 객체를 생성하자
                me = User(user_data[0], user_data[1], user_data[2])
                break

    if me == None:
        print("아이디 또는 비밀번호가 일치하지 않습니다")
    else:
        print("로그인이 성공했습니다")

    return me


if __name__ == "__main__":
    me = None
    while True:
        if me == None:
            choice = int(input("회원가입(0) vs 로그인(1): "))

            if choice == 0:
                sign_up()
            else:
                me = log_in()
        else:
            menu = input(f"{me.get_name()}님 환영합니다\n메뉴를 선택하세요\n\t게시글 작성(0)\n\t로그아웃(1)\n\t:")
            if menu == 0:
                pass
            else:
                me = None
