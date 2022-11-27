from collections import deque


def check_correct(s):
    # 큐에 오픈하는 가로를 삽입한다
    # 닫는 괄호가 나오면 그게 마지막으로 삽입한 오픈 괄호의 짝인지 확인한다
    # 맞으면 정상적으로 팝
    # 모두 팝 되면 올바른 괄호 문자열이다
    open_symbols = ["(", "[", "{"]
    close_symbols = [")", "]", "}"]
    q = []
    for i in range(len(s)):
        if s[i] in open_symbols:
            q.append(s[i])
        else:
            if len(q) == 0:
                return False
            last_input_symbol = q.pop()
            index = open_symbols.index(last_input_symbol)
            if close_symbols[index] == s[i]:
                continue
            else:
                return False
    if len(q) == 0:
        return True
    else:
        return False


def solution(s):
    s = deque(list(s))
    cnt = 0
    result = check_correct(s)
    if result == True:
        cnt += 1
    for i in range(1, len(s)):
        front = s.popleft()
        s.append(front)
        result = check_correct(s)
        if result == True:
            cnt += 1
    return cnt