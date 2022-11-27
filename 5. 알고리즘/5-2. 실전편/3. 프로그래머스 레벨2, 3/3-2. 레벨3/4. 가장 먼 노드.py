import heapq


def dijkstra_fast_ver(graph, min_distances, start_node):
    q = []
    heapq.heappush(q, [0, start_node])
    min_distances[start_node] = 0

    while q:
        [dist, current_node] = heapq.heappop(q)
        if min_distances[current_node] < dist:
            continue
        for next_node in graph[current_node]:
            cost = min_distances[current_node] + next_node[1]
            if cost < min_distances[next_node[0]]:
                min_distances[next_node[0]] = cost
                heapq.heappush(q, [cost, next_node[0]])


def solution(n, edge):
    edge.sort()
    graph = [[] for _ in range(n + 1)]
    for one_edge in edge:
        graph[one_edge[0]].append([one_edge[1], 1])
        graph[one_edge[1]].append([one_edge[0], 1])

    INF = 1e9
    min_distances = [INF] * (n + 1)
    dijkstra_fast_ver(graph, min_distances, 1)
    min_distances = sorted(min_distances[1:])
    max_value = max(min_distances[1:])

    return n - (min_distances.index(max_value) + 1) + 1

# 다익스트라
solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]])
