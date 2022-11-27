def solution(rows, columns, queries):
    answer = []

    matrix = [[None for _ in range(columns + 1)] for _ in range(rows + 1)]
    for row in range(1, rows + 1):
        for col in range(1, columns + 1):
            matrix[row][col] = ((row - 1) * columns + col)
    # for row in range(rows + 1):
    #     for col in range(columns + 1):
    #         print(matrix[row][col], end=" ")
    #     print()
    # 22 23 24
    # 32    34
    # 42    44
    # 52 53 54
    for query in queries:
        [start_row, start_col, end_row, end_col] = query
        temp = matrix[start_row][start_col]
        min_value = temp
        for row in range(start_row + 1, end_row + 1):
            matrix[row - 1][start_col] = matrix[row][start_col]
            if matrix[row][start_col] < min_value:
                min_value = matrix[row][start_col]
        for col in range(start_col + 1, end_col + 1):
            matrix[end_row][col - 1] = matrix[end_row][col]
            if matrix[end_row][col] < min_value:
                min_value = matrix[end_row][col - 1]
        for row in range(end_row - 1, start_row - 1, - 1):
            matrix[row + 1][end_col] = matrix[row][end_col]
            if matrix[row][end_col] < min_value:
                min_value = matrix[row][end_col]
        for col in range(end_col - 1, start_col - 1, -1):
            matrix[start_row][col + 1] = matrix[start_row][col]
            if matrix[start_row][col] < min_value:
                min_value = matrix[start_row][col]
        matrix[start_row][start_col + 1] = temp

        # for row in range(rows + 1):
        #     for col in range(columns + 1):
        #         print(matrix[row][col], end=" ")
        #     print()
        # print(min_value)
        answer.append(min_value)
    # print(answer)
    return answer


solution(6, 6, [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]])
