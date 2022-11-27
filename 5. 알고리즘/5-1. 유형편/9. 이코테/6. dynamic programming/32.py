n = int(input())
number_triangle = [list(map(int, input().split(" "))) for _ in range(n)]
dp_table = [[0] * (i + 1) for i in range(n)]

dp_table[0][0] = number_triangle[0][0]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            dp_table[i][j] = dp_table[i - 1][j] + number_triangle[i][j]
        elif j == i:
            dp_table[i][j] = dp_table[i - 1][j - 1] + number_triangle[i][j]
        else:
            dp_table[i][j] = max(dp_table[i - 1][j - 1], dp_table[i - 1][j]) + number_triangle[i][j]
print(max(dp_table[n - 1]))
