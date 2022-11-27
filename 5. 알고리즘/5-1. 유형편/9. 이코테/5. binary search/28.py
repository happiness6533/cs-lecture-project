def binary_search(iter, start, end):
    if start > end:
        return -1

    mid = (start + end) // 2

    if iter[mid] == mid:
        return mid
    elif iter[mid] < mid:
        return binary_search(iter, mid + 1, end)
    else:
        return binary_search(iter, start, mid - 1)


n = int(input())
numbers = list(map(int, input().split(" ")))
print(binary_search(numbers, 0, len(numbers) - 1))
