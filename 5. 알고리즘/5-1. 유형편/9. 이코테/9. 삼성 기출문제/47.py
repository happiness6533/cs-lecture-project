# 아직 덜 품
graph = [[],
         [],
         [],
         []]
for i in range(4):
    row_input = list(map(int, input().split(" ")))
    graph[i].append([row_input[0], row_input[1]])
    graph[i].append([row_input[2], row_input[3]])
    graph[i].append([row_input[4], row_input[5]])
    graph[i].append([row_input[6], row_input[7]])

d_row = [-1, -1, 0, 1, 1, 1, 0, -1]
d_col = [0, -1, -1, -1, 0, 1, 1, 1]


def fish_move(row, col, direction, shark_row, shark_col):
    direction_index = direction - 1
    for i in range(8):
        direction_index %= 8
        next_row = row + d_row[direction_index]
        next_col = col + d_col[direction_index]

        if next_row < 0 or next_row > 3 or next_col < 0 or next_col > 3:  # 다음 위치가 범위 초과
            continue
        if next_row == shark_row and next_col == shark_col:  # 다음 위치가 상어
            continue

        graph[row][col][0], graph[next_row][next_col][0] = graph[next_row][next_col][0], graph[row][col][0]
        graph[row][col][1], graph[next_row][next_col][1] = graph[next_row][next_col][1], graph[row][col][1]
        break


def fish_move_all(shark_row, shark_col):
    move_count = 0
    while move_count <= 16:
        for i in range(4):
            for j in range(4):
                if i == shark_row and j == shark_col:  # 상어는 움직이지 않는다
                    continue
                if graph[i][j][0] == (i * 4) + j + 1:
                    fish_move(i, j, graph[i][j][1], shark_row, shark_col)
                    move_count += 1
                    print((i * 4) + j + 1, move_count)


def find_food_dfs(row, col, prev_eat, max_eat):
    visited[row][col] = 1
    max_eat = max(max_eat, prev_eat + graph[row][col][0])

    fish_move_all(row, col)
    direction_index = graph[row][col][1] - 1
    next_row = row
    next_col = col
    for i in range(3):
        next_row = next_row + d_row[direction_index]
        next_col = next_col + d_col[direction_index]

        if next_row < 0 or next_row > 3 or next_col < 0 or next_col > 3:
            break
        if visited[next_row][next_col] != 0:
            continue

        find_food_dfs(next_row, next_col, visited[row][col], max_eat)

    return max_eat


visited = [[0] * 4 for i in range(4)]
visited[0][0] = graph[0][0][0]
print(find_food_dfs(0, 0, 0, 0))
