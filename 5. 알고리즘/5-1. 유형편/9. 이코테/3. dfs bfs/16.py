from itertools import combinations
from copy import deepcopy
from collections import deque

# 7 7
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0

n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]
virus_visited_memo = [[False] * m for _ in range(n)]
# 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]
original_wall_cnt = 0
virus_coords = []
empty_spaces = []
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_spaces.append([i, j])
        elif graph[i][j] == 1:
            original_wall_cnt += 1
        elif graph[i][j] == 2:
            virus_coords.append([i, j])


# 코테 문제 풀이 생각 순서
# 1. 가능한 모든 벽 세우기를 다 해보고 그 중에서 안전구역이 최대인걸 고르자 = 완전 탐색 방법
# => 혹시 시간 초과 또는 메모리 초과가 예상된다면? => 문제의 입력에 힌트가 있다
# => 62c3 = 60 * 60 * 60 / 6 = 36000 => 완전 탐색 충분
# => 만약 1000만번이 넘어가는 시간 복잡도라면 아래의 방법을 고려하자

# 2. 도대체 벽을 어떻게 신박하게 세워야 안전구역이 최대가 되지? = 똑똑이 풀이법

# 우선 벽을 3개를 세우는 모든 경우를 생각하자
# 그 중 하나의 경우에 대해서 벽을 세우고 => 바이러스를 퍼져 나가게 만들어보자(bfs) => 안전 구역을 계산해서 => 이게 최대인가 확인!

# 벽 3개를 세우는 방법1(쉬운 버전)
# empty_spaces = []
# for i in range(n):
#     for j in range(m):
#         if graph[i][j] == 0:
#             empty_spaces.append([i, j])
#
# combinations_results = list(combinations(empty_spaces, 3))
# print(len(combinations_results))


# 벽 3개를 세우는 방법2(어려운 버전)
# 완전 탐색 전략1: for문과 while문: 완전 탐색의 대상이 이미 다 주어진 경우
# 완전 탐색 전략2: DFS(for문과 재귀의 절묘한 조합 + 메모장) / BFS(큐의 푸쉬와 팝을 통한 절묘한 순서 + 메모장): 완전 탐색의 대상을 직접 생성해야 하는 경우
# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
def dfs(graph, walls_memo, current_node, combinations_results_by_dfs):
    walls_memo.append(current_node)
    if len(walls_memo) == 3:
        combinations_results_by_dfs.append(walls_memo)
        return
    for i in range(walls_memo[-1][0], n):
        start_col = walls_memo[-1][1] if i == walls_memo[-1][0] else 0
        for j in range(start_col, m):
            if [i, j] in walls_memo:
                continue
            if graph[i][j] != 0:
                continue
            next_node = [i, j]
            copy_walls_memo = deepcopy(walls_memo)
            dfs(graph, copy_walls_memo, next_node, combinations_results_by_dfs)


combinations_results_by_dfs = []
for empty_space in empty_spaces:
    dfs(graph, [], empty_space, combinations_results_by_dfs)


# 완전 탐색 전략2 예제
# a, b, c => aaa, aab, aac, ... ccc
# answer = ""
# for first in ['a', 'b', 'c']:
#     answer += first
#     for second in ['a', 'b', 'c']:
#         answer += second
#         for third in ['a', 'b', 'c']:
#             answer += third
#             print(answer)
#             answer = answer[:2]
#         answer = answer[:1]
#     answer = ""

# a, b, c => aaa, aab, aac, ... ccc
# 인접 리스트: [a, b, c], count
# def dfs(graph, str_memo, current_node):
#     str_memo += current_node
#     if len(str_memo) == 3:
#         print(str_memo)
#     next_nodes = ['a', 'b', 'c'] if len(str_memo) <= 2 else []
#     for next_node in next_nodes:
#         dfs(graph, str_memo, next_node)
# dfs(['a', 'b', 'c'], '', 'a')
# dfs(['a', 'b', 'c'], '', 'b')
# dfs(['a', 'b', 'c'], '', 'c')


# a, b, c => aaa, aab, aac, ... ccc
# 인접 리스트: [a, b, c], count
# def dfs(graph, str_memo, current_node):
#     str_memo += current_node
#     print(str_memo)
#     if len(str_memo) == 3:
#         print(str_memo)
#         return
#     for next_node in ['a', 'b', 'c']:
#         dfs(graph, str_memo, next_node)
#
#
# dfs(['a', 'b', 'c'], '', 'a')


# a, b, c => aaa, aab, aac, ... ccc
# 인접 리스트: [a, b, c], count
# def dfs(graph, str_memo, current_node):
#     str_memo.append(current_node)
#     if len(str_memo) == 3:
#         print("".join(str_memo))
#         return
#     for next_node in ['a', 'b', 'c']:
#         # 1. 문제 발생 코드
#         # copy_str_memo = str_memo
#         # 2. 올바른 코드지만 복잡
#         # copy_str_memo = []
#         # for value in str_memo:
#         #     copy_str_memo.append(value)
#         # 3. 올바른 코드인데 간단
#         copy_str_memo = deepcopy(str_memo)
#         dfs(graph, copy_str_memo, next_node)
#
#
#
# dfs(['a', 'b', 'c'], [], 'a')

# 2 0 0 0 1 1 0
# 0 0 1 0 1 2 0
# 0 1 1 0 1 0 0
# 0 1 0 0 0 0 0
# 0 0 0 0 0 1 1
# 0 1 0 0 0 0 0
# 0 1 0 0 0 0 0
def bfs(graph, memo, start_nodes):
    queue = deque()
    for start_node in start_nodes:
        queue.append(start_node)
        memo[start_node[0]][start_node[1]] = True
    while queue:
        current_node = queue.popleft()
        for i in range(len(d_row)):
            next_node_row = current_node[0] + d_row[i]
            next_node_col = current_node[1] + d_col[i]
            if next_node_row < 0 or next_node_row > n - 1 or next_node_col < 0 or next_node_col > m - 1:
                continue
            if memo[next_node_row][next_node_col] == True:
                continue
            if graph[next_node_row][next_node_col] == 1:
                continue
            next_node = [next_node_row, next_node_col]
            queue.append(next_node)
            memo[next_node_row][next_node_col] = True


max_safe_cnt = 0
for combinations_result in combinations_results_by_dfs:
    # 벽 3개를 세우자
    copy_graph = deepcopy(graph)
    for wall_coord in combinations_result:
        copy_graph[wall_coord[0]][wall_coord[1]] = 1
    # 바이러스를 퍼뜨리자(bfs)
    copy_virus_visited_memo = deepcopy(virus_visited_memo)

    bfs(copy_graph, copy_virus_visited_memo, virus_coords)

    virus_cnt = 0
    for i in range(n):
        for j in range(m):
            if copy_virus_visited_memo[i][j] == True:
                virus_cnt += 1
    # 안전구역 계산
    safe_cnt = n * m - original_wall_cnt - 3 - virus_cnt
    if safe_cnt > max_safe_cnt:
        max_safe_cnt = safe_cnt
print(max_safe_cnt)
