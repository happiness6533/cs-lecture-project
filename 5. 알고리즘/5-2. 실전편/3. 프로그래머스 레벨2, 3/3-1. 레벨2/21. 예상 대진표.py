def solution(n,a,b):
    # 12 34 56 78
    # 1  2  3  4
    #    1  2
    a = a
    b = b
    count = 1
    while True:
        if abs(a - b) == 1:
            if a < b:
                if b % 2 == 0:
                    break
            if a > b:
                if a % 2 == 0:
                    break
        a = (a + 1) // 2
        b = (b + 1) // 2
        count += 1

    return count