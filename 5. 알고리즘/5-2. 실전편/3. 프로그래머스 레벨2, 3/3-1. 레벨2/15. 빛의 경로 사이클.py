from copy import deepcopy

d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]


def get_next(grid, prev_coord, current_coord):
    prev_d_row = current_coord[0] - prev_coord[0]
    prev_d_col = current_coord[1] - prev_coord[1]

    current_dir = grid[current_coord[0]][current_coord[1]]
    grid_row_len = len(grid)
    grid_col_len = len(grid[0])
    next_coord = None
    if current_dir == "S":
        next_coord = [(current_coord[0] + prev_d_row) % grid_row_len, current_coord[1] + prev_d_col]
    elif current_dir == "L":
        # -1 0 => 0 -1
        # 1 0 => 0 1
        # 0 -1 => 1 0
        # 0 1 => -1 0
        if prev_d_row == -1 and prev_d_col == 0:
            next_coord = [current_coord[0] % grid_row_len, (current_coord[1] - 1) % grid_col_len]
        elif prev_d_row == 1 and prev_d_col == 0:
            next_coord = [current_coord[0] % grid_row_len, (current_coord[1] + 1) % grid_col_len]
        elif prev_d_row == 0 and prev_d_col == -1:
            next_coord = [(current_coord[0] + 1) % grid_row_len, current_coord[1] % grid_col_len]
        elif prev_d_row == 0 and prev_d_col == 1:
            next_coord = [(current_coord[0] - 1) % grid_row_len, current_coord[1] % grid_col_len]
    elif current_dir == "R":
        # -1 0 => 0 1
        # 1 0 => 0 -1
        # 0 -1 => -1 0
        # 0 1 => 1 0
        if prev_d_row == -1 and prev_d_col == 0:
            next_coord = [current_coord[0] % grid_row_len, (current_coord[1] + 1) % grid_col_len]
        elif prev_d_row == 1 and prev_d_col == 0:
            next_coord = [current_coord[0] % grid_row_len, (current_coord[1] - 1) % grid_col_len]
        elif prev_d_row == 0 and prev_d_col == -1:
            next_coord = [(current_coord[0] - 1) % grid_row_len, current_coord[1] % grid_col_len]
        elif prev_d_row == 0 and prev_d_col == 1:
            next_coord = [(current_coord[0] + 1) % grid_row_len, current_coord[1] % grid_col_len]

    return next_coord


def try_cycle(grid, memo, prev_coord, current_coord):
    next_coord = get_next(grid, prev_coord, current_coord)
    current_d_row = next_coord[0] - current_coord[0]
    current_d_col = next_coord[1] - current_coord[1]
    # 상 하 좌 우
    if current_d_row == -1 and current_d_col == 0:
        if memo[0] == True:
            return True
        memo[0] = True
    elif current_d_row == 1 and current_d_col == 0:
        if memo[1] == True:
            return True
        memo[1] = True
    elif current_d_row == 0 and current_d_col == -1:
        if memo[2] == True:
            return True
        memo[2] = True
    elif current_d_row == 0 and current_d_col == 1:
        if memo[3] == True:
            return True
        memo[3] = True
    try_cycle(grid, memo, current_coord, next_coord)


def solution(grid):
    memo = [[[False] * 4 for j in range(len(grid[0]))] for i in range(len(grid))]
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(len(d_row)):
                copy_memo = deepcopy(memo)
                next_coord = try_cycle(grid, copy_memo, [i + d_row[k], j + d_col[k]], [i, j])


solution(["SL",
          "LR"])
