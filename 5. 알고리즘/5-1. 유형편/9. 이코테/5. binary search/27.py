import sys

# 만약에 이 방법으로 문자열을 받아야 하는 경우 문자열 마지막의 엔터를 처리해야 한다
input = sys.stdin.readline
n, x = map(int, input().split(" "))
numbers = list(map(int, input().split(" ")))


def binary_min_search(iter, start, end, target):
    if start > end:
        return None

    mid = (start + end) // 2

    if iter[mid] == target:
        if mid == 0:
            return mid
        elif iter[mid - 1] == target:
            return binary_min_search(iter, start, mid - 1, target)
        else:
            return mid
    elif iter[mid] < target:
        return binary_min_search(iter, mid + 1, end, target)
    else:
        return binary_min_search(iter, start, mid - 1, target)


def binary_max_search(iter, start, end, target):
    if start > end:
        return None

    mid = (start + end) // 2

    if iter[mid] == target:
        if mid == n - 1:
            return mid
        elif iter[mid + 1] == target:
            return binary_max_search(iter, mid + 1, end, target)
        else:
            return mid
    elif iter[mid] < target:
        return binary_max_search(iter, mid + 1, end, target)
    else:
        return binary_max_search(iter, start, mid - 1, target)


min_index = binary_min_search(numbers, 0, n - 1, x)
if min_index is None:
    print(-1)
else:
    max_index = binary_max_search(numbers, 0, n - 1, x)
    print(max_index - min_index + 1)
