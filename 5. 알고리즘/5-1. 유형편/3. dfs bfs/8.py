from collections import deque


def dfs(visited, current_row, current_col, row, col, dRow, dCol):
    visited[current_row][current_col] = 1

    for i in range(len(dRow)):
        next_row = current_row + dRow[i]
        next_col = current_col + dCol[i]

        if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
            continue
        if graph[next_row][next_col] == 1:
            continue
        if visited[next_row][next_col] == 1:
            continue

        dfs(visited, next_row, next_col, row, col, dRow, dCol)


def bfs(visited, start_row, start_col, row, col, dRow, dCol):
    queue = deque([[start_row, start_col]])
    visited[start_row][start_col] = 1

    while queue:
        coordinate = queue.popleft()
        for i in range(len(dRow)):
            next_row = coordinate[0] + dRow[i]
            next_col = coordinate[1] + dCol[i]

            if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
                continue
            if graph[next_row][next_col] == 1:
                continue
            if visited[next_row][next_col] == 1:
                continue

            queue.append([next_row, next_col])
            visited[next_row][next_col] = 1


if __name__ == "__main__":
    row, col = map(int, input().split(' '))
    graph = [list(map(int, input())) for _ in range(row)]
    visited = [[0] * col for _ in range(row)]

    dRow = [0, 0, 1, -1]
    dCol = [1, -1, 0, 0]

    count = 0
    for i in range(row):
        for j in range(col):
            if graph[i][j] == 0 and visited[i][j] == 0:
                dfs(visited, i, j, row, col, dRow, dCol)
                # bfs(visited, i, j, row, col, dRow, dCol)
                count += 1

    print(count)
