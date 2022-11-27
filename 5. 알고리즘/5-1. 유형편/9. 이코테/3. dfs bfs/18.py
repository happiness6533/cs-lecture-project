def make_correct_v(v):
    if v == "":
        return v

    count = 0
    is_correct_u = None
    if v[0] == "(":
        count += 1
        is_correct_u = True
    else:
        count -= 1
        is_correct_u = False

    for i in range(1, len(v)):
        if v[i] == "(":
            count += 1
        else:
            count -= 1

        if count == 0:
            sub_u = v[0:i + 1]
            sub_v = v[i + 1:]
            if is_correct_u:
                v = sub_u + make_correct_v(sub_v)
            else:
                v = "(" + make_correct_v(sub_v) + ")"
                new_sub_u = ""
                for j in range(1, len(sub_u) - 1):
                    if sub_u[j] == "(":
                        new_sub_u += ")"
                    else:
                        new_sub_u += "("
                v += new_sub_u
            break

    return v


def solution(string):
    answer = make_correct_v(string)

    return answer


print(solution(")))((("))
