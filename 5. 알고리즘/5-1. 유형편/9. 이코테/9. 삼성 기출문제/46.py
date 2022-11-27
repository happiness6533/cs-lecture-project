from collections import deque


def bfs(graph, visited, start_row, start_col, row, col, dRow, dCol):
    queue = deque([[start_row, start_col]])
    visited[start_row][start_col] = 0
    graph[start_row][start_col] = 0

    while queue:
        coordinate = queue.popleft()
        for i in range(len(dRow)):
            next_row = coordinate[0] + dRow[i]
            next_col = coordinate[1] + dCol[i]

            if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
                continue
            if graph[next_row][next_col] > size:
                continue
            if visited[next_row][next_col] != 0:
                continue

            queue.append([next_row, next_col])
            visited[next_row][next_col] = visited[coordinate[0]][coordinate[1]] + 1

            if 1 <= graph[next_row][next_col] < size:
                results.append([visited[next_row][next_col], next_row, next_col])


# 1. 입력 받기
n = int(input())
graph = [list(map(int, input().split(" "))) for _ in range(n)]  # 문제의 정보

# 2. 초기값 세팅
start_row = 0
start_col = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            start_row = i
            start_col = j
            break
graph[start_row][start_col] = 0
size = 2
count = 0
total_time = 0

# 3. 추가적인 세팅
dRow = [0, 0, 1, -1]
dCol = [1, -1, 0, 0]

# 4. 문제 해결
while True:
    results = []
    visited = [[0] * n for _ in range(n)]  # 새로운 정보를 기록할 공간
    bfs(graph, visited, start_row, start_col, n, n, dRow, dCol)
    if len(results) == 0:
        print(total_time)
        break

    results.sort(key=lambda x: (x[0], x[1], x[2]))
    total_time += results[0][0]
    start_row = results[0][1]
    start_col = results[0][2]

    graph[start_row][start_col] = 0

    count += 1
    if count == size:
        size += 1
        count = 0
