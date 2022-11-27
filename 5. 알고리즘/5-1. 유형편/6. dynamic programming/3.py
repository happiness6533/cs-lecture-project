n = int(input())


# 방법1
def func(x):
    if x == 1:
        return 1
    if x == 2:
        return 3
    return func(x - 1) + 2 * func(x - 2)


print(func(n) % 796796)

# 방법2
dp_table = [0 for _ in range(n + 1)]
dp_table[1] = 1
dp_table[2] = 3
current = 3
while True:
    dp_table[current] = dp_table[current - 1] + 2 * dp_table[current - 2]
    if current == n:
        print(dp_table[n] % 796796)
        break
    current += 1
