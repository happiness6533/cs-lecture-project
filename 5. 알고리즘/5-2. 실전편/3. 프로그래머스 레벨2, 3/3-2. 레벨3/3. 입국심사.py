# 배열에서 30을 찾아라 => 찾은 값이 30을 만족하는 조건을 만족하는걸 찾아라
# 어떤 조건 아래에 최소값을 찾아라 => 이분 탐색으로 조건을 만족하는 값 중 최소를 찾는다
# 1. 이 문제가 이분탐색로 해결 가능하다는 것을 생각할 수 있는 것이 중요
# 2. start와 end의 그 경계에 대해 생각을 정리해 둘 것

def binary_search(start, end, n, times):
    if start >= end:
        return start

    mid = (start + end) // 2
    count = 0
    for time in times:
        count += mid // time

    if count == n:
        return binary_search(start, mid, n, times)
    elif count > n:
        return binary_search(start, mid - 1, n, times)
    else:
        return binary_search(mid + 1, end, n, times)


def solution(n, times):
    times.sort()

    min_total_time = times[0]
    max_total_time = times[-1] * n
    return binary_search(min_total_time, max_total_time, n, times)

# 이분탐색
print(solution(10, [6, 8, 10]))
