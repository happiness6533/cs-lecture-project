import sys

input = sys.stdin.readline
n, c = map(int, input().split(" "))
homes = [int(input()) for _ in range(n)]
homes.sort()


def can_build_all_share(mid, homes, c):
    # mid 거리가 최소인 방식으로 c개의 공유기를 주어진 집에 설치할 수 있는가?
    # 1 2   4     8 9
    share_cnt = 1
    share_index = 0
    i = 1
    while i < n:
        dist = homes[i] - homes[share_index]
        if dist >= mid:
            share_cnt += 1
            share_index = i
            if share_cnt == c:
                break
        i += 1

    if share_cnt == c:
        return True
    else:
        return False


def binary_search(start, end, homes, c):
    mid = (start + end) // 2

    if can_build_all_share(mid, homes, c) == True:
        if can_build_all_share(mid + 1, homes, c) == True:
            return binary_search(mid + 1, end, homes, c)
        else:
            return mid
    else:
        return binary_search(start, mid - 1, homes, c)


# 1 <= 공유기 사이 거리중에 최소값 <= homes[n - 1] - homes[0]
result = binary_search(1, homes[n - 1] - homes[0], homes, c)
print()
print(result)
