from abc import *


class User(metaclass=ABCMeta):
    # 데이터: 인스턴스 변수, 클래스 변수
    # 함수: 인스턴스 메소드, 클래스 메소드, 스태틱 메소드, 매직 메소드, 추상 메소드

    # 클래스 변수
    __count = 0

    # 클래스 메소드
    @classmethod
    def get_count(cls):
        return cls.__count

    @classmethod
    def plus_one_count(cls):
        cls.__count += 1

    # 스태틱 메소드
    @staticmethod
    def say_hi():
        print("하이하이")

    # 매직 메소드
    def __init__(self, user_id, user_password, nick_name):
        # 인스턴스 변수(protected, private)
        self._user_id = user_id  # 자식까지는 이 변수에 접근 가능 = protected
        self._nick_name = nick_name
        self.__user_password = user_password  # 모두가 접근 불가능 = private
        User.plus_one_count()

    # 인스턴스 메소드
    def get_user_id(self):
        return self._user_id

    def set_user_id(self, new_user_id):
        self._user_id = new_user_id

    def set_password(self, original_password, new_password):
        if original_password == self.__user_password:
            self.__user_password = new_password
        else:
            print("비밀번호가 일치하지 않습니다")

    def get_nick_name(self):
        return self._nick_name

    # 추상 메소드
    @abstractmethod
    def introduce_myself(self):
        pass

    @abstractmethod
    def get_user_type(self):
        pass


class Influencer(User):
    def __init__(self, user_id, user_password, nick_name):
        # 부모님 변수 그대로 상속 ㄱ
        super(Influencer, self).__init__(user_id, user_password, nick_name)
        # 나만의 재산
        self.company = None

    def get_nick_name(self):
        return f"세상 핫한 {self._nick_name}"

    def introduce_myself(self):
        print(f"안녕? 나는 요즘 핫한 {self._user_id}임")

    def set_company(self, company):
        self.company = company

    def show_company(self):
        return self.company.brand_name

    def get_user_type(self):
        return "influencer"


class Company(User):
    # 1. 브랜드 네임 변수 추가
    # 2. 인플루언서 목록 변수 추가
    # 3. 인플루언서를 추가하는 메소드 만들기
    # 4. 모든 인플루언서의 이름만 차례대로 출력하는 메소드 만들기
    def introduce_myself(self):
        print(f"안녕? 나는 거대 기업의 수장인 {self._user_id}임")

    def get_user_type(self):
        return "company"


if __name__ == "__main__":
    influencer1 = Influencer("julie", 1234, "뿡뿡이")
    influencer2 = Influencer("sully", 1234, "빵빵이")
    company = Company("semi", 5678, "뽕뽕이", "kakao")

    influencer1.set_company(company)
    print(influencer1.set_company())
    influencer2.set_company(company)
    print(influencer2.set_company())

    company.add_influencer(influencer1)
    company.add_influencer(influencer2)

    company.show_all_names_of_influencer()
