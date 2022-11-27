# 방법1: 플로이드 워셜 알고리즘
# INF = int(1e9)
#
# n, m = map(int, input().split(' '))
# graph = [[INF] * (n + 1) for _ in range(n + 1)]
# for i in range(m):
#     a, b = map(int, input().split(' '))
#     graph[a][b] = 1
#     graph[b][a] = 1
# for i in range(1, n + 1):
#     graph[i][i] = 0
# x, k = map(int, input().split(' '))
#
# for k in range(1, n + 1):
#     for a in range(1, n + 1):
#         for b in range(1, n + 1):
#             graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])
#
# if graph[1][k] + graph[k][x] >= INF:
#     print(-1)
# else:
#     print(graph[1][k] + graph[k][x])

# 방법2: 다익스트라 알고리즘
import heapq

INF = int(1e9)

n, m = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append([b, 1])
    graph[b].append([a, 1])
x, k = map(int, input().split(' '))


def dijkstra(start, distance):
    q = []
    heapq.heappush(q, [0, start])
    distance[start] = 0
    while q:
        dist, node_number = heapq.heappop(q)
        if distance[node_number] < dist:
            continue
        for next_node_info in graph[node_number]:
            cost = dist + next_node_info[1]
            if cost < distance[next_node_info[0]]:
                distance[next_node_info[0]] = cost
                heapq.heappush(q, [cost, next_node_info[0]])


distance = [INF] * (n + 1)
dijkstra(1, distance)
dist_1 = distance[k]

distance = [INF] * (n + 1)
dijkstra(k, distance)
dist_2 = distance[x]

print(dist_1 + dist_2)
