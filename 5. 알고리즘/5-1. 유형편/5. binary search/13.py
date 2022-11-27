def binary_search(iter, start, end, target):
    if start > end:
        return None

    mid = (start + end) // 2

    if iter[mid] == target:
        return mid
    elif iter[mid] < target:
        return binary_search(iter, mid + 1, end, target)
    else:
        return binary_search(iter, start, mid - 1, target)


import sys

n = int(input())
parts = list(map(int, sys.stdin.readline().rstrip().split(' ')))
m = int(input())
reqs = list(map(int, sys.stdin.readline().rstrip().split(' ')))

parts.sort()
for req in reqs:
    if req == 9:
        print(req)
    if binary_search(parts, 0, n - 1, req) is not None:
        print("yes", end=' ')
    else:
        print("no", end=' ')
