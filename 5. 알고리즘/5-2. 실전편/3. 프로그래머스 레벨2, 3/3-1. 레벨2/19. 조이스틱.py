def check_all_a(name):
    for char in name:
        if char != 'A':
            return False
    return True


def solution(name):
    answer1 = 0
    for i in range(len(name)):
        char = name[i]
        diff1 = abs(ord('A') - ord(char))
        diff2 = 26 - diff1
        answer1 += min(diff1, diff2)
        print(i, min(diff1, diff2))
        if check_all_a(name[i + 1:]):
            answer1 -= i
            break
    answer1 = answer1 + (len(name) - 1)

    answer2 = 0
    for i in range(0, -len(name), -1):
        char = name[i]
        diff1 = abs(ord('A') - ord(char))
        diff2 = 26 - diff1
        print(i, min(diff1, diff2))
        answer2 += min(diff1, diff2)
        if i == -(len(name) - 1) and name[i] == 'A':
            answer2 -= 1
    answer2 = answer2 + (len(name) - 1)

    return min(answer1, answer2)