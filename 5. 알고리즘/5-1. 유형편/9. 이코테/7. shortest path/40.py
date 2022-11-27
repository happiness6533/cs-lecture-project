import heapq

INF = int(1e9)


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


n, m = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append([b, 1])
    graph[b].append([a, 1])

distance = [INF] * (n + 1)
dijkstra(1, distance)
d = max(distance[1:])
print(distance.index(d), end=' ')
print(d, end=' ')
count = 0
for i in range(len(distance)):
    if distance[i] == d:
        count += 1
print(count)
