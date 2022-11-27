n = int(input())
stored_foods = list(map(int, input().split(" ")))
total_get_foods = [0 for _ in range(n)]

total_get_foods[0] = stored_foods[0]
total_get_foods[1] = stored_foods[1]
total_get_foods[2] = stored_foods[2] + stored_foods[0]
for i in range(2, n):
    total_get_foods[i] = max(total_get_foods[i - 2], total_get_foods[i - 3]) + stored_foods[i]

print(max(total_get_foods))
