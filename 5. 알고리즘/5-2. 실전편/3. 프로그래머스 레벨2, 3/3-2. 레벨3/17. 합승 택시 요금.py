import heapq

d_row = [1, -1, 0, 0]
d_col = [0, 0, 1, -1]


def bfs(graph, visited, start_node_num):
    pq = []
    heapq.heappush(pq, [0, start_node_num])
    visited[start_node_num] = 0
    while pq:
        [dist, current_node_num] = heapq.heappop(pq)
        for next_node in graph[current_node_num]:
            [added_fare, next_node_num] = next_node
            next_dist = dist + added_fare
            next_node = [next_dist, next_node_num]
            if visited[next_node_num] != 1e9:
                if visited[next_node_num] <= next_dist:
                    continue
            heapq.heappush(pq, next_node)
            visited[next_node_num] = next_dist


def solution(n, s, a, b, fares):
    graph = [None]
    graph += [[] for _ in range(n)]
    for i in range(len(fares)):
        [c, d, fare] = fares[i]
        graph[c].append([fare, d])
        graph[d].append([fare, c])

    visited = [None]
    visited += [1e9] * n
    bfs(graph, visited, s)

    min_value = 1e9
    for i in range(1, n + 1):
        new_visited = [None]
        new_visited += [1e9] * n
        bfs(graph, new_visited, i)
        new_value = visited[i] + new_visited[a] + new_visited[b]
        if new_value < min_value:
            min_value = new_value

    return min_value