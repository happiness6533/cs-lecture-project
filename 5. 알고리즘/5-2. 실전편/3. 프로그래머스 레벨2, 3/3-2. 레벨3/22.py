def solution(board, skill):
    for s in skill:
        for row in range(s[1], s[3] + 1):
            for col in range(s[2], s[4] + 1):
                if s[0] == 1:
                    board[row][col] -= s[5]
                else:
                    board[row][col] += s[5]

    alive_cnt = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] >= 1:
                alive_cnt += 1

    return alive_cnt


solution([[5, 5, 5, 5, 5],
          [5, 5, 5, 5, 5],
          [5, 5, 5, 5, 5],
          [5, 5, 5, 5, 5]],
         [[1, 0, 0, 3, 4, 4], [1, 2, 0, 2, 3, 2], [2, 1, 0, 3, 1, 2], [1, 0, 1, 3, 3, 1]])
