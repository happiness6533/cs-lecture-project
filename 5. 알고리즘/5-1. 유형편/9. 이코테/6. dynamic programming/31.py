import sys

input = sys.stdin.readline
t = int(input())
for i in range(t):
    n, m = map(int, input().split(" "))
    numbers = list(map(int, input().split(" ")))
    gold_map = [[] for _ in range(n)]
    max_gold_map = [[] for _ in range(n)]
    for row in range(n):
        for col in range(m):
            gold_map[row].append(numbers[row * m + col])
            max_gold_map[row].append(0)

    if n == 1:
        print(sum(gold_map))
        continue

    for row in range(n):
        max_gold_map[row][0] = gold_map[row][0]

    for col in range(1, m):
        for row in range(n):
            if row == 0:
                max_gold_map[row][col] = max(max_gold_map[row][col - 1],
                                             max_gold_map[row + 1][col - 1]) + gold_map[row][col]
            elif row == n - 1:
                max_gold_map[row][col] = max(max_gold_map[row - 1][col - 1],
                                             max_gold_map[row][col - 1]) + gold_map[row][col]
            else:
                max_gold_map[row][col] = max(max_gold_map[row - 1][col - 1],
                                             max_gold_map[row][col - 1],
                                             max_gold_map[row + 1][col - 1]) + gold_map[row][col]

    print(max(list(map(lambda x: x[m - 1], max_gold_map))))
