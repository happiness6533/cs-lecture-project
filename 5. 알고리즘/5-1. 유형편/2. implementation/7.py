if __name__ == "__main__":
    row, col = map(int, input().split(" "))
    position_row, position_col, direction = map(int, input().split(" "))
    game_map = []
    for i in range(row):
        game_map.append(list(map(int, input().split(" "))))

    # 위 오 아래 왼
    dRow = [-1, 0, 1, 0]
    dCol = [0, 1, 0, -1]

    result = 1
    game_map[position_row][position_col] = -1
    while True:
        stopFlag = False
        for i in range(1, 5):
            direction = ((direction - 1) + 4) % 4
            if game_map[position_row + dRow[direction]][position_col + dCol[direction]] == 1:
                if i == 4:
                    stopFlag = True
                    break
                else:
                    continue
            if game_map[position_row + dRow[direction]][position_col + dCol[direction]] == -1:
                if i == 4:
                    direction = ((direction - 2) + 4) % 4
                    position_row += dRow[direction]
                    position_col += dCol[direction]
                    break
                else:
                    continue
            position_row += dRow[direction]
            position_col += dCol[direction]
            game_map[position_row][position_col] = -1
            result += 1
            break
        if stopFlag:
            break

    print(result)
