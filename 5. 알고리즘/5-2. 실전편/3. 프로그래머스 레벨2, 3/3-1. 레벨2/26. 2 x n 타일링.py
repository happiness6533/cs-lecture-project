def solution(n):
    answer = 0

    a1 = 1
    a2 = 2
    for i in range(3, n + 1):
        answer = a1 + a2
        a1 = a2
        a2 = answer
    answer %= 1000000007

    return answer