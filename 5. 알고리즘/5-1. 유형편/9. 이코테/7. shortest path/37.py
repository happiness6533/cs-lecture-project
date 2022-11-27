# 입력
n = int(input())
m = int(input())
INF = 1e9
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split(" "))
    graph[a][b] = min(c, graph[a][b])
for i in range(1, n + 1):
    graph[i][i] = 0

# 플로이드 워셜 알고리즘
for middle in range(1, n + 1):
    for start in range(1, n + 1):
        for end in range(1, n + 1):
            graph[start][end] = min(graph[start][end], graph[start][middle] + graph[middle][end])

# 정답
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j] if graph[i][j] != INF else 0, end=" ")
    print()