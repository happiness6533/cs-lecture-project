def solution(n):
    answer = ""

    while n != 0:
        rest = n % 3
        n = n // 3
        if rest == 0:
            rest = 3
            n -= 1
        if rest == 3:
            rest = 4
        answer = str(rest) + answer

    return answer
