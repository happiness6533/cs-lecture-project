n, m = map(int, input().split(' '))
coins = []
for i in range(n):
    new_coin = int(input())
    coins.append(new_coin)

dp_table = [0 for _ in range(m + 1)]
for coin in coins:
    dp_table[coin] = 1

flag = False
current = 1
while True:
    for coin in coins:
        if current + coin <= m:
            if dp_table[current + coin] == 0 and dp_table[current] != 0:
                dp_table[current + coin] = dp_table[current] + 1
            else:
                dp_table[current + coin] = min(dp_table[current] + 1, dp_table[current + coin])
    if dp_table[m] != 0:
        flag = True
        print(dp_table[m])
        break
    current += 1
# 뇌내망상 뇌피셜 금지 허허허...
if not flag:
    print(-1)
