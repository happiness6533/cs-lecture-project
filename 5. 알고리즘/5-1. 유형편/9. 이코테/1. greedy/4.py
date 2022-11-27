# 5
# 3 2 1 1 9
# 1 1 2 3 9

# 1 2 3: 이미 그 금액의 동전이 있거나
# 4 = 2 + 1 + 1: 그 금액보다 작은 동전의 합
# 5 = 3 + 2
# 6 = 3 + 2 + 1
# 7 = 3 + 2 + 1 + 1
# --------------------------------
# 8 = 3 + 2 + 1 + 1 + ?... : 그 금액보다 작은 동전의 합으로 8 불가능
# 1. 내가 다 해봣어ㄷㄷ진짜 안됨 => 완전탐색 => for / 재귀(dfs) / 큐(bfs, 다익스트라) / 다이나믹
# 2. 특정 조건을 따져서 해결 => 그리디

# 평범한 사람의 풀이
from itertools import combinations


def get_all_sums(coins, total_sum):
    # [1 1 2 3], 4
    print(coins, total_sum)
    for cnt in range(2, len(coins) + 1):
        results = combinations(coins, cnt)
        for result in results:
            if sum(result) == total_sum:
                return True
    return False


n = int(input())
coins = list(map(int, input().split()))
coins.sort()
coin_sum = sum(coins)
for total_sum in range(1, coin_sum + 1):
    print(total_sum)
    if total_sum in coins:
        continue
    temp_coins = []
    for coin in coins:
        if coin < total_sum:
            temp_coins.append(coin)
        else:
            break
    if get_all_sums(temp_coins, total_sum) == True:
        continue
    print(total_sum)
    break

# 똑똑한 사람의 풀이
# 5
# 3 2 1 1 9
# 1 1 2 3 9
n = int(input())
coins = list(map(int, input().split()))
coins.sort()

total_sum = 1
for coin in coins:
    if total_sum >= coin:
        total_sum += coin
    else:
        break
print(total_sum)
