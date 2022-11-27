import heapq


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


INF = int(1e9)
n, m, c = map(int, input().split(" "))
graph = [[] for _ in range(n + 1)]
for i in range(m):
    x, y, z = map(int, input().split(" "))
    graph[x].append([y, z])
distance = [INF] * (n + 1)
dijkstra(c, distance)

count = 0
max_distance = 0
for i in range(1, n + 1):
    if i == c or distance[i] == INF:
        continue
    count += 1
    max_distance = max(distance[i], max_distance)

print(count, max_distance)
