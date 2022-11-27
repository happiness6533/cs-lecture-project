if __name__ == "__main__":
    # 1. 모듈 패키지 from import * as 정의파트 실행파트 __name__ __main__ __init__.py
    import random
    from python.python1 import users_array  # python1의 코드가 1회 실행된다

    # chosen_index = []
    # while len(chosen_index) != 3:
    #     random_index = random.randint(0, 4)
    #     if random_index not in chosen_index:
    #         chosen_index.append(random_index)
    #         print(users_array[random_index]["name"])
    #
    # while True:
    #     random_index = random.randint(0, 4)
    #     if random_index not in chosen_index:
    #         chosen_index.append(random_index)
    #         print(users_array[random_index]["name"])
    #         if len(chosen_index) == 3:
    #             break

    # 2. txt 파일 쓰고 읽기, input
    user_file = open("users.txt", "w", encoding="utf-8")
    while True:
        name = input("유저의 이름을 입력하세요: ")
        if name == "exit":
            break
        age = int(input("유저의 출생연도를 입력하세요: "))
        user_file.write(f"{name} {age}\n")
    user_file.close()

    user_file = open("users.txt", "r", encoding="utf-8")
    while True:
        line = user_file.readline()
        print(line)
        if not line:
            break
        print(line, end='')
    user_file.close()

    # 3. csv 파일 읽고 쓰기
    import csv

    user_csv_file = open('users.csv', 'w', encoding="utf-8", newline="\n")
    wr = csv.writer(user_csv_file)
    wr.writerow([1, "하하맨", 2001])
    wr.writerow([2, "호호걸", 2002])
    user_csv_file.close()

    user_csv_file = open('users.csv', 'r', encoding="utf-8")
    rdr = csv.reader(user_csv_file)
    for line in rdr:
        print(line[1])
    user_csv_file.close()

    # 4. 바이너리 파일 쓰고 읽기, with
    import pickle

    user = {"name": "권예빈", "age": 100}

    # 컨텍스트 매니저 with
    with open('users.b', 'wb') as file:
        pickle.dump(user, file)

    with open('users.b', 'rb') as file:
        user = pickle.load(file)

    # 5. 예외처리
    try:
        x = int(input("나눌 숫자를 입력하세요: "))
        y = 10 / x
        print(y)
    except:
        print("예외가 발생했습니다.")

    y = [10, 20, 30]
    try:
        index, x = map(int, input("인덱스와 나눌 숫자를 입력하세요: ").split())
        print(y[index] / x)
    except ZeroDivisionError:
        print("숫자를 0으로 나눌 수 없습니다.")
    except IndexError:
        print("으잉?")

    try:
        index, x = map(int, input("인덱스와 나눌 숫자를 입력하세요: ").split())
        print(y[index] / x)
    except ZeroDivisionError as e:
        print("숫자를 0으로 나눌 수 없습니다.", e)
    except IndexError as e:
        print("잘못된 인덱스입니다.", e)

    try:
        index, x = map(int, input("인덱스와 나눌 숫자를 입력하세요: ").split())
        print(y[index] / x)
    except Exception as e:
        print(e)

    try:
        x = int(input("나눌 숫자를 입력하세요: "))
        y = 10 / x
    except ZeroDivisionError:
        print("숫자를 0으로 나눌 수 없습니다.")
    else:
        print(y)

    try:
        x = int(input("나눌 숫자를 입력하세요: "))
        y = 10 / x
    except ZeroDivisionError:
        print("숫자를 0으로 나눌 수 없습니다.")
    else:
        print(y)
    finally:
        print("코드 실행이 끝났습니다.")

    try:
        x = int(input("3의 배수를 입력하세요: "))
        if x % 3 != 0:
            raise Exception("3의 배수가 아닙니다.")
        print(x)
    except Exception as e:
        print("예외가 발생했습니다.", e)


    class NotThreeMultipleError(Exception):
        def __init__(self):
            super().__init__("3의 배수가 아닙니다.")


    try:
        x = int(input("3의 배수를 입력하세요: "))
        if x % 3 != 0:
            raise NotThreeMultipleError
        print(x)
    except Exception as e:
        print("예외가 발생했습니다.", e)
