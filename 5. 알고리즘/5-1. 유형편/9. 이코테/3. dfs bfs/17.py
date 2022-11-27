from collections import deque


def bfs(visited, start_coords, row, col, dRow, dCol, s):
    queue = deque()
    for coord in start_coords:
        queue.append(coord)

    while queue:
        coordinate = queue.popleft()
        for i in range(len(dRow)):
            next_row = coordinate[0] + dRow[i]
            next_col = coordinate[1] + dCol[i]

            if visited[coordinate[0]][coordinate[1]] == s:
                continue
            if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
                continue
            if graph[next_row][next_col] != 0:
                continue

            queue.append([next_row, next_col])
            visited[next_row][next_col] = visited[coordinate[0]][coordinate[1]] + 1
            graph[next_row][next_col] = graph[coordinate[0]][coordinate[1]]


n, k = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]
s, x, y = map(int, input().split(" "))

dRow = [0, 0, 1, -1]
dCol = [1, -1, 0, 0]
start_coords = []
visited = [[-1] * n for _ in range(n)]
for virus_number in range(1, k + 1):
    for row in range(n):
        for col in range(n):
            if graph[row][col] == virus_number:
                start_coords.append([row, col])
                visited[row][col] = 0

bfs(visited, start_coords, n, n, dRow, dCol, s)
print(graph[x - 1][y - 1])
