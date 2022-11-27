from auth import *
from user import *
from post import *

if __name__ == "__main__":
    me = None
    while True:
        try:
            if me is None:
                choice = int(input("로그인(0) / 회원가입(1): "))
                if choice == 0:
                    email = input("이메일을 입력하세요: ")
                    password = input("비밀번호를 입력하세요: ")
                    me = log_in(email, password, me)
                    if me is None:
                        print("이메일 혹은 비밀번호가 일치하지 않습니다")
                elif choice == 1:
                    email = input("이메일을 입력하세요: ")
                    password = input("비밀번호를 입력하세요: ")
                    id = input("사용할 아이디를 입력하세요: ")
                    sign_up(email, password, id)
                else:
                    print("입력이 잘못되었습니다")
            else:
                choice = int(input(f"\t{me['id']}님 메뉴를 선택하세요\n"
                                   f"\t1. 비밀번호 변경\n"
                                   f"\t2. 로그아웃\n"
                                   f"\t3. 게시글 목록 보기\n"
                                   f"\t4. 게시글 작성하기\n"
                                   f"\t:"))
                if choice == 1:
                    old_password = input("\t원래의 비밀번호를 입력하세요: ")
                    new_password = input("\t변경할 비밀번호를 입력하세요: ")
                    change_flag = update_password(me, old_password, new_password)
                    if change_flag == True:
                        print("\t비밀번호가 변경되었습니다. 다시 로그인하세요")
                        me = log_out(me)
                    else:
                        print("\t이메일 또는 비밀번호가 일치하지 않습니다.")
                elif choice == 2:
                    me = log_out(me)
                    print("\t로그아웃 되었습니다")
                elif choice == 3:
                    my_posts = load_post(me)
                    print(f"\t{me['id']}님의 게시글")
                    for post in my_posts:
                        print(f"\t{post['content']}")
                    print()
                elif choice == 4:
                    content = input("게시글을 적어주세요: ")
                    make_post(me, content)
        except Exception as e:
            print(e)
