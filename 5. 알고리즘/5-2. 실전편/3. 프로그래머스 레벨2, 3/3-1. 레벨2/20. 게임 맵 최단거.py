import heapq

d_row = [1, -1, 0, 0]
d_col = [0, 0, 1, -1]


def bfs(graph, visited, start_node_coord, n, m):
    pq = []
    heapq.heappush(pq, [1, start_node_coord])
    visited[start_node_coord[0]][start_node_coord[1]] = 1
    while pq:
        [dist, current_node_coord] = heapq.heappop(pq)
        for i in range(4):
            next_node_row = current_node_coord[0] + d_row[i]
            next_node_col = current_node_coord[1] + d_col[i]
            if next_node_row < 0 or next_node_row > n - 1 or next_node_col < 0 or next_node_col > m - 1:
                continue
            if graph[next_node_row][next_node_col] == 0:
                continue

            next_dist = dist + 1
            next_node_coord = [next_node_row, next_node_col]
            next_node = [next_dist, next_node_coord]

            if visited[next_node_row][next_node_col] != -1:
                if visited[next_node_row][next_node_col] <= next_dist:
                    continue

            heapq.heappush(pq, next_node)
            visited[next_node_coord[0]][next_node_coord[1]] = next_dist


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])
    visited = [[-1] * m for _ in range(n)]
    bfs(maps, visited, [0, 0], n, m)

    return visited[n - 1][m - 1]