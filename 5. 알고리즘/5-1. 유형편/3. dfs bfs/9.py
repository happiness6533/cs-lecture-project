from collections import deque


def bfs(visited, start_row, start_col, row, col, dRow, dCol):
    queue = deque([[start_row, start_col]])
    visited[start_row][start_col] = 1
    graph[start_row][start_col] = 1

    flag = False
    while queue:
        coordinate = queue.popleft()
        for i in range(len(dRow)):
            next_row = coordinate[0] + dRow[i]
            next_col = coordinate[1] + dCol[i]

            if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
                continue
            if graph[next_row][next_col] == 0:
                continue
            if visited[next_row][next_col] == 1:
                continue

            queue.append([next_row, next_col])
            visited[next_row][next_col] = 1
            graph[next_row][next_col] = graph[coordinate[0]][coordinate[1]] + 1

            if next_row == row - 1 and next_col == col - 1:
                flag = True
                break

        if flag:
            return


if __name__ == "__main__":
    row, col = map(int, input().split(' '))
    graph = [list(map(int, input())) for _ in range(row)]
    visited = [[0] * col for _ in range(row)]

    dRow = [0, 0, 1, -1]
    dCol = [1, -1, 0, 0]

    start_row = 0
    start_col = 0
    bfs(visited, start_row, start_col, row, col, dRow, dCol)

    print(graph[row - 1][col - 1])

    # 5 6
    # 101010
    # 111111
    # 000011
    # 111110
    # 111111

    # 입력
    row, col = map(int, input().split(" "))
    graph = [list(map(int, input())) for _ in range(row)]
    # 메모장
    visited = [[0] * col for _ in range(row)]
    print(graph)
    print(visited)


    def dfs(graph, visited, current_node, count):
        visited[current_node[0]][current_node[1]] = count
        count += 1
        if current_node[0] == row - 1 and current_node[1] == col - 1:
            return
        for i in range(len(d_row)):
            next_row = current_node[0] + d_row[i]
            next_col = current_node[1] + d_col[i]
            if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
                continue
            if visited[next_row][next_col] != 0:
                continue
            if graph[next_row][next_col] == 0:
                continue
            next_node = [next_row, next_col]
            dfs(graph, visited, next_node, count)


    d_row = [0, 1, 0, -1]
    d_col = [1, 0, -1, 0]

    # print(dfs(graph, visited, [0, 0], 1))
    # for i in range(len(visited)):
    #     print(visited[i])

    from collections import deque


    def bfs(graph, visited, start_node):
        queue = deque()
        queue.append(start_node)
        visited[start_node[0]][start_node[1]] = 1
        while queue:
            current_node = queue.popleft()
            for i in range(len(d_row)):
                next_row = current_node[0] + d_row[i]
                next_col = current_node[1] + d_col[i]
                if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
                    continue
                if visited[next_row][next_col] != 0:
                    continue
                if graph[next_row][next_col] == 0:
                    continue
                next_node = [next_row, next_col]
                queue.append(next_node)
                visited[next_node[0]][next_node[1]] = visited[current_node[0]][current_node[1]] + 1


    print(bfs(graph, visited, [0, 0]))
    for i in range(len(visited)):
        print(visited[i])

    print(visited[row - 1][col - 1])