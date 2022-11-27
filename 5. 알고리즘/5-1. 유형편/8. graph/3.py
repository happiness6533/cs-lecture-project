from collections import deque


def topology_sort():
    q = deque()

    for i in range(1, n + 1):
        if in_degree[i] == 0:
            q.append(i)

    while q:
        current_node = q.popleft()
        for linked_node in graph[current_node]:
            in_degree[linked_node] -= 1
            total_times[linked_node] = max(total_times[linked_node], total_times[current_node] + times[linked_node])
            if in_degree[linked_node] == 0:
                q.append(linked_node)


n = int(input())
graph = [[] for i in range(n + 1)]
in_degree = [0] * (n + 1)
times = [0] * (n + 1)
total_times = [0] * (n + 1)
for i in range(1, n + 1):
    line = list(map(int, input().split(" ")))
    node = i
    time = line[0]
    times[node] = time
    total_times[node] = time
    for j in range(1, len(line) - 1):
        if line[j] == -1:
            break
        graph[line[j]].append(node)
        in_degree[node] += 1

topology_sort()
for total_time in total_times[1:]:
    print(total_time)
