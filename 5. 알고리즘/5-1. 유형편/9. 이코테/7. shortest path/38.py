from collections import deque

n, m = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)


def bfs(graph, start_node, visited):
    queue = deque([start_node])
    visited[start_node] = 1

    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = 1


def bfs2(graph, start_node, visited, target_node):
    queue = deque([start_node])
    visited[start_node] = 1

    result = False
    while queue:
        node = queue.popleft()
        for next_node in graph[node]:
            if visited[next_node] == -1:
                queue.append(next_node)
                visited[next_node] = 1
            if next_node == target_node:
                result = True
                return result

    return result


count = 0
for start_node in range(1, n + 1):
    visited = [-1] * (n + 1)
    bfs(graph, start_node, visited)
    unvisited_nodes = []
    for i in range(1, n + 1):
        if visited[i] == -1:
            unvisited_nodes.append(i)
    finalFlag = True
    for unvisited_node in unvisited_nodes:
        visited = [-1] * (n + 1)
        result = bfs2(graph, unvisited_node, visited, start_node)
        if result == False:
            finalFlag = False
            break
    if finalFlag == True:
        count += 1

print(count)
