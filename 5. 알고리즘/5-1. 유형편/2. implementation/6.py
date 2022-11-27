if __name__ == "__main__":
    position = input()

    row = int(position[1])
    col = ord(position[0]) % ord("a") + 1
    d_rows = [2, 2, -2, -2, 1, 1, -1, -1]
    d_cols = [1, -1, 1, -1, 2, -2, 2, -2]

    result = 0
    for i in range(len(d_rows)):
        if (row + d_rows[i] < 1) or (row + d_rows[i] > 8) or (col + d_cols[i] < 1) or (col + d_cols[i] > 8):
            continue
        result += 1

    print(result)
