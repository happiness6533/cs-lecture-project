def binary_search(iter, start, end, target):
    if start > end:
        return end

    mid = (start + end) // 2

    sum_of_lengths = 0
    for length in iter:
        if length > mid:
            sum_of_lengths += (length - mid)

    if sum_of_lengths == target:
        return mid
    elif sum_of_lengths < target:
        return binary_search(iter, start, mid - 1, target)
    else:
        return binary_search(iter, mid + 1, end, target)


n, m = map(int, input().split(' '))
cakes = sorted(list(map(int, input().split(' '))))
length = binary_search(cakes, 0, max(cakes), m)
print(length)
