from collections import deque
from copy import deepcopy
import heapq

INF = 1E9


def bfs(graph, info, copy_find_sheep_cnt_memo, start_node_number):
    q = deque()
    copy_find_sheep_cnt_memo[start_node_number] = 0
    q.append(start_node_number)
    while q:
        current_node_number = q.popleft()
        if info[current_node_number] == 0:
            return copy_find_sheep_cnt_memo[current_node_number]

        for next_node_number in graph[current_node_number]:
            if copy_find_sheep_cnt_memo[next_node_number] != INF:
                continue
            copy_find_sheep_cnt_memo[next_node_number] = copy_find_sheep_cnt_memo[current_node_number] + 1
            q.append(next_node_number)

    return INF


def dijkstra(graph, info, visited_memo, start_node_number, total_sheep_cnt, total_wolf_cnt):
    pq = []
    heapq.heappush(pq, [graph[start_node_number][0], start_node_number])
    while pq:
        [cnt, current_node_number] = heapq.heappop(pq)
        if len(pq) != 0:
            history = []
            history.append([cnt, current_node_number])
            [cnt_2, current_node_number_2] = heapq.heappop(pq)
            while cnt_2 == cnt:
                history.append([cnt_2, current_node_number_2])
                if len(pq) != 0:
                    [cnt_2, current_node_number_2] = heapq.heappop(pq)
                else:
                    break
            if cnt_2 != cnt:
                heapq.heappush(pq, [cnt_2, current_node_number_2])
            if len(history) > 1:
                max_sheep_history = [history[0][0], history[0][1]]
                max_future_cnt = dijkstra(graph, info, deepcopy(visited_memo), max_sheep_history[1], total_sheep_cnt, total_wolf_cnt)
                for i in range(1, len(history)):
                    future_cnt = dijkstra(graph, info, deepcopy(visited_memo), history[i][1], total_sheep_cnt, total_wolf_cnt)
                    if max_future_cnt < future_cnt:
                        max_future_cnt = future_cnt
                        max_sheep_history = history[i]
                for i in range(len(history)):
                    if history[i] == max_sheep_history:
                        continue
                    heapq.heappush(pq, history[i])
                [cnt, current_node_number] = max_sheep_history
        # print(current_node_number, cnt, total_sheep_cnt, total_wolf_cnt)
        if info[current_node_number] == 0:
            total_sheep_cnt += 1
        else:
            total_wolf_cnt += 1
            if cnt == INF or total_sheep_cnt == total_wolf_cnt:
                return total_sheep_cnt
        # print(current_node_number, cnt, total_sheep_cnt, total_wolf_cnt)
        visited_memo[current_node_number] = True
        for next_node_number in graph[current_node_number][1]:
            if visited_memo[next_node_number] == True:
                continue
            heapq.heappush(pq, [graph[next_node_number][0], next_node_number])
    return total_sheep_cnt


def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    for edge in edges:
        [parent_node, child_node] = edge
        graph[parent_node].append(child_node)
    find_sheep_cnt_memo = [INF] * len(info)

    copy_graph = deepcopy(graph)
    for node_number in range(len(info)):
        copy_find_sheep_cnt_memo = deepcopy(find_sheep_cnt_memo)
        find_sheep_cnt = bfs(copy_graph, info, copy_find_sheep_cnt_memo, node_number)
        graph[node_number] = [find_sheep_cnt, copy_graph[node_number]]

    visited_memo = [False] * len(info)
    return dijkstra(graph, info, visited_memo, 0, 0, 0)


solution([0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0],
         [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [4, 8], [6, 9], [9, 10]])
# solution([0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
#          [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]])
