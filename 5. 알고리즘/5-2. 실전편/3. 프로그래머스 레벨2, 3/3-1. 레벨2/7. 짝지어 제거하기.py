


def solution(s):
    # baabaa
    s_list = list(s)
    i = 0
    while i <= len(s_list) - 2:
        if s_list[i] == s_list[i + 1]:
            del s_list[i]
            del s_list[i]
            if i != 0:
                i -= 1
        else:
            i += 1
    if len(s_list) == 0:
        return 1
    else:
        return 0

solution("aa")