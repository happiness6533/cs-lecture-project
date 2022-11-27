from collections import deque


def bfs(graph, visited, start_row, start_col, row, col, d_row, d_col, country_number):
    queue = deque([[start_row, start_col]])
    visited[start_row][start_col] = country_number
    count = 1

    while queue:
        coordinate = queue.popleft()
        for i in range(len(d_row)):
            next_row = coordinate[0] + d_row[i]
            next_col = coordinate[1] + d_col[i]

            if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
                continue
            if not l <= abs(graph[coordinate[0]][coordinate[1]] - graph[next_row][next_col]) <= r:
                continue
            if visited[next_row][next_col] != 0:
                continue

            queue.append([next_row, next_col])
            visited[next_row][next_col] = country_number

            mean = graph[coordinate[0]][coordinate[1]] * count + graph[next_row][next_col] // (count + 1)
            graph[next_row][next_col] = mean
            count += 1

    if count == 1:
        return False
    else:
        return True


n, l, r = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

d_row = [0, 0, 1, -1]
d_col = [1, -1, 0, 0]

result = False
while True:
    for row in range(n):
        for col in range(n):
            visited = [[0] * n for _ in range(n)]
            country_number = 1
            if visited[row][col] == 0:
                united_result = bfs(graph, visited, row, col, n, n, d_row, d_col, country_number)
                if united_result == True:
                    result = True
                country_number += 1
