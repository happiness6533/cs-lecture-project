# 가로 방향 + 회전1 체크
def rotation_check_1(board, current_coord):
    if current_coord[2] - 1 < 0:
        return False
    if board[current_coord[2] - 1][current_coord[3]] == 1:
        return False
    return True


def rotation_check_2(board, current_coord):
    if current_coord[0] - 1 < 0:
        return False
    if board[current_coord[0] - 1][current_coord[1]] == 1:
        return False
    return True


def rotation_check_3(board, current_coord):
    if current_coord[2] + 1 > len(board) - 1:
        return False
    if board[current_coord[2] + 1][current_coord[3]] == 1:
        return False
    return True


def rotation_check_4(board, current_coord):
    if current_coord[0] + 1 > len(board) - 1:
        return False
    if board[current_coord[0] + 1][current_coord[1]] == 1:
        return False
    return True


def dfs(board, current_coord, visited):
    # 현재 케이스를 체크하고
    # 방향 = 0(가로), 1(수직)
    visited.append(current_coord)

    # 좌우, 4회전
    d_move_1 = [0, 0, -1, 0, 1, 0]
    d_move_2 = [-1, 1, 0, 1, 0, 1]
    d_move_3 = [0, 0, 0, -1, 0, 0]
    d_move_4 = [-1, 1, -1, 0, -1, 1]
    # 가능한 다음 이동에 대해서
    for i in range(6):
        # 가로방향 로봇
        if current_coord[-1] == 0:


            check = True
            if i == 2:
                check = rotation_check_1(board, current_coord)
            if i == 3:
                check = rotation_check_2(board, current_coord)
            if i == 4:
                check = rotation_check_3(board, current_coord)
            if i == 5:
                check = rotation_check_4(board, current_coord)

            if check is False:
                continue

            next_coord_row_1 = current_coord[0] + d_move_1[i]
            next_coord_col_1 = current_coord[1] + d_move_2[i]
            next_coord_row_2 = current_coord[2] + d_move_3[i]
            next_coord_col_2 = current_coord[3] + d_move_4[i]

            if next_coord_row_1 < 0 or next_coord_row_1 > len(
                    board) - 1 or next_coord_col_1 < 0 or next_coord_col_1 > len(board) - 1:
                continue
            if next_coord_row_2 < 0 or next_coord_row_2 > len(
                    board) - 1 or next_coord_col_2 < 0 or next_coord_col_2 > len(board) - 1:
                continue
            if board[next_coord_row_1][next_coord_col_1] == 1:
                continue
            if board[next_coord_row_2][next_coord_col_2] == 1:
                continue

            if i == 0 or i == 1:
                if [next_coord_row_1, next_coord_col_1, next_coord_row_2, next_coord_col_2, current_coord[-1]] in visited:
                    continue
                dfs(board, [next_coord_row_1, next_coord_col_1, next_coord_row_2, next_coord_col_2, current_coord[-1]], visited)
            else:
                if [next_coord_row_1, next_coord_col_1, next_coord_row_2, next_coord_col_2, 1 - current_coord[-1]] in visited:
                    continue
                dfs(board, [next_coord_row_1, next_coord_col_1, next_coord_row_2, next_coord_col_2, 1 - current_coord[-1]], visited)


    # 이미 체크한 경우가 아니라면
    # 재귀


def solution(board):
    dfs([0, 0, 0, 1, 0])
    return 1


solution([[0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0],
          [0, 1, 0, 1, 1],
          [1, 1, 0, 0, 1],
          [0, 0, 0, 0, 0]])
