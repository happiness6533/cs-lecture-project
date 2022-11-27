n = int(input())
k = int(input())
graph = [[0] * n for _ in range(n)]
for _ in range(k):
    row, col = map(int, input().split(" "))
    graph[row][col] = -1


def move_snake(graph, head_row, head_col, pre_direction, tail_row, tail_col):
    next_head_row = head_row
    next_head_col = head_col

    if pre_direction == "up":
        next_head_row -= 1
    elif pre_direction == "down":
        next_head_row += 1
    elif pre_direction == "left":
        next_head_col -= 1
    elif pre_direction == "right":
        next_head_col += 1

    if next_head_row < 0 or next_head_row > n - 1 or next_head_col < 0 or next_head_col > n - 1:
        return -1, -1, None, -1, -1
    if graph[next_head_row][next_head_col] >= 1:
        return -1, -1, None, -1, -1

    if graph[next_head_row][next_head_col] == 0:  # 사과 x
        graph[next_head_row][next_head_col] = graph[head_row][head_col] + 1
        graph[tail_row][tail_col] = 0
        d_row = [1, -1, 0, 0]
        d_col = [0, 0, 1, -1]
        min_body = 1e9
        for i in range(len(d_row)):
            temp_next_tail_row = tail_row + d_row[i]
            temp_next_tail_col = tail_col + d_col[i]
            if temp_next_tail_row < 0 or temp_next_tail_row > n - 1 or temp_next_tail_col < 0 or temp_next_tail_col > n - 1:
                continue
            if graph[temp_next_tail_row][temp_next_tail_col] == 0:
                continue
            if graph[temp_next_tail_row][temp_next_tail_col] == -1:
                continue
            if graph[temp_next_tail_row][temp_next_tail_col] < min_body:
                next_tail_row = temp_next_tail_row
                next_tail_col = temp_next_tail_col
                min_body = graph[next_tail_row][next_tail_col]

    elif graph[next_head_row][next_head_col] == -1:  # 사과 o
        graph[next_head_row][next_head_col] = graph[head_row][head_col] + 1
        next_tail_row = tail_row
        next_head_col = tail_col

    return next_head_row, next_head_col, pre_direction, next_tail_row, next_tail_col


l = int(input())
head_row = 0
head_col = 0
tail_row = 0
tail_col = 0
graph[head_row][head_col] = 1
pre_direction = "right"
total_time = 0
for _ in range(l):
    time, direction = input().split(" ")
    time = int(time)
    end_flag = False
    for i in range(time):
        head_row, head_col, pre_direction, tail_row, tail_col = move_snake(graph,
                                                                           head_row, head_col,
                                                                           pre_direction,
                                                                           tail_row, tail_col)
        if head_row == -1:
            end_flag = True
            total_time += (i + 1)
            break
    if not end_flag:
        total_time += time
    else:
        break
    if direction == "L":
        if pre_direction == "up":
            pre_direction = "left"
        elif pre_direction == "down":
            pre_direction = "left"
        elif pre_direction == "left":
            pre_direction = "down"
        elif pre_direction == "right":
            pre_direction = "up"
    elif direction == "D":
        if pre_direction == "up":
            pre_direction = "right"
        elif pre_direction == "down":
            pre_direction = "right"
        elif pre_direction == "left":
            pre_direction = "up"
        elif pre_direction == "right":
            pre_direction = "down"

print(total_time)
