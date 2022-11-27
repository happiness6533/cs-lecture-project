import sys
from collections import deque

input = sys.stdin.readline
n, m, k, x = map(int, input().split(" "))

# 1. 그래프 만들기
graph = [None]
graph += [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split(" "))
    graph[a].append(b)
memo = [None]
INF = 1e9
memo += [INF] * n


# 2. 모든 노드에 방문하기
# 2-1. dfs = 완전 탐색을 재귀 호출 + 메모장으로
def dfs(graph, memo, prev_node, current_node):
    # 현재 노드까지 이동 거리 = 바로 직전에 있던 노드까지 이동 거리 + 1
    # 새롭게 알게 된 현재 노드까지 이동 거리가 메모장에 적혀있는 최단 이동 거리보다 더 짧은가?
    # 만약 그렇다면 값을 업데이트
    current_node_dist = memo[prev_node] + 1
    if current_node_dist < memo[current_node]:
        memo[current_node] = current_node_dist
    # print(memo)
    for next_node in graph[current_node]:
        dfs(graph, memo, current_node, next_node)


# 2-2. bfs = 완전 탐색을 큐 + 메모장으로
def bfs(graph, memo, start_node):
    q = deque()

    q.append(start_node)
    memo[start_node] = 0
    while q:
        current_node = q.popleft()
        for next_node in graph[current_node]:
            if memo[next_node] != INF:
                continue
            q.append(next_node)
            memo[next_node] = memo[current_node] + 1


# 2-3. 초기 값 설정이 중요하다
memo[x] = 0
# dfs(graph, memo, x, x)
bfs(graph, memo, x)

# 3. 출력
results = []
for i in range(1, n + 1):
    if memo[i] == k:
        results.append(i)
if len(results) == 0:
    print(-1)
else:
    results.sort()
    for result in results:
        print(result)
