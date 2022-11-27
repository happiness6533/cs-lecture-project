import heapq

INF = int(1e9)
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]


def dijkstra(start_coordinate, distance):
    q = []
    heapq.heappush(q, [0, start_coordinate])
    distance[start_coordinate[0]][start_coordinate[1]] = 0
    while q:
        dist, coordinate = heapq.heappop(q)
        if distance[coordinate[0]][coordinate[1]] < dist:
            continue
        for i in range(len(d_row)):
            next_row = coordinate[0] + d_row[i]
            next_col = coordinate[1] + d_col[i]
            if next_row < 0 or next_col < 0 or next_row > n - 1 or next_col > n - 1:
                continue
            cost = dist + graph[next_row][next_col]
            if cost < distance[next_row][next_col]:
                distance[next_row][next_col] = cost
                heapq.heappush(q, [cost, [next_row, next_col]])


t = int(input())
for _ in range(t):
    n = int(input())
    graph = [list(map(int, input().split(" "))) for _ in range(n)]
    distance = [[INF] * n for _ in range(n)]
    dijkstra([0, 0], distance)
    print(distance[n - 1][n - 1] + graph[0][0])
