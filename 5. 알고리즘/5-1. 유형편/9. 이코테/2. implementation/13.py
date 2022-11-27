from itertools import combinations
from collections import deque

d_row = [0, 0, 1, -1]
d_col = [1, -1, 0, 0]


def get_chickien_distance(graph, home, choice, visited):
    min_dist = 1e9
    for chicken_position in choice:
        dist = abs(home[0] - chicken_position[0]) + abs(home[1] - chicken_position[1])
        # print(dist, home, choice)
        if dist < min_dist:
            min_dist = dist
    return min_dist
    # q = deque([home])
    # visited[home[0]][home[1]] = 1
    #
    # while q:
    #     coordinate = q.popleft()
    #     for i in range(len(d_row)):
    #         next_row = coordinate[0] + d_row[i]
    #         next_col = coordinate[1] + d_col[i]
    #
    #         if next_row < 0 or next_row > row - 1 or next_col < 0 or next_col > col - 1:
    #             continue
    #         if [next_row, next_col] in choice:
    #             return graph[coordinate[0]][coordinate[1]] + 1
    #         if visited[next_row][next_col] != 0:
    #             continue
    #
    #         q.append([next_row, next_col])
    #         visited[next_row][next_col] = visited[coordinate[0]][coordinate[1]]


def get_total_chickien_distance(graph, homes, choice):
    total_chickien_distance = 0
    for home in homes:
        visited = [[0] * n for _ in range(n)]
        total_chickien_distance += get_chickien_distance(graph, home, choice, visited)
    return total_chickien_distance


n, m = map(int, input().split(" "))
graph = [list(map(int, input().split(" "))) for _ in range(n)]

homes = []
chickiens = []
for row in range(n):
    for col in range(n):
        if graph[row][col] == 1:
            homes.append([row, col])
        if graph[row][col] == 2:
            chickiens.append([row, col])
choices = combinations(chickiens, m)

min_chickien_dist = 1e9
for choice in choices:
    dist = get_total_chickien_distance(graph, homes, choice)
    if dist < min_chickien_dist:
        min_chickien_dist = dist

print(min_chickien_dist)
