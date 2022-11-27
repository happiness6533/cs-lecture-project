# 수업
def sign_up(email, password, id):
    if isEmail(email) is False:
        print("이메일 형식이 올바르지 않습니다")
        return

    if isEnoughComplexPassword(password) is False:
        print("비밀번호가 너무 간단합니다")
        return

    if isUniqueEmail(email) is False:
        print("중복된 이메일입니다")
        return

    if isUniqueId(email) is False:
        print("중복된 이메일입니다")
        return

    file = open("users.txt", "a", encoding="utf8")
    file.write(f"{email} {password} {id}\n")
    file.close()


# 수업
def log_in(email, password, me):
    if me is not None:
        return me

    file = open("users.txt", "r", encoding="utf8")
    lines = file.readlines()
    for line in lines:
        line_array = line.strip().split(" ")
        stored_email = line_array[0]
        stored_password = line_array[1]
        stored_id = line_array[2]
        if stored_email == email and stored_password == password:
            file.close()
            me = {"email": stored_email, "password": stored_password, "id": stored_id}
            break

    return me


# 수업
def log_out(me):
    me = None
    return me


# 퀴즈
def isEmail(email):
    pass


# 퀴즈
def isEnoughComplexPassword(password):
    pass


# 퀴즈
def isUniqueEmail(email):
    pass


# 퀴즈
def isUniqueId(email):
    pass
