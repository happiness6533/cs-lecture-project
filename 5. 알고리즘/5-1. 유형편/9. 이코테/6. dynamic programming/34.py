n = int(input())
numbers = list(map(int, input().split(" ")))

max_numbers = [n] * n
for i in range(len(numbers) - 1):
    if numbers[i] > numbers[i + 1]:
        max_numbers[i + 1] = max_numbers[i]
    elif numbers[i] == numbers[i + 1]:
        max_numbers[i + 1] = max_numbers[i] - 1
    else:
        left_count = 0
        right_count = 0
        for left in reversed(numbers[:i + 1]):
            if left <= numbers[i + 1]:
                left_count += 1
            else:
                break
        for right in numbers[i + 1:]:
            if right >= numbers[i]:
                right_count += 1
            else:
                break

        # if left_count > right_count:
        #     max_numbers[i + 1] = max_numbers[i] - right_count
        # elif left_count < right_count:
        #     max_numbers[i + 1] = max_numbers[i] - left_count
        # else:
        max_numbers[i + 1] = max_numbers[i] - left_count
# print(max_numbers)
print(n - min(max_numbers))
