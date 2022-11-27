from copy import deepcopy
from itertools import combinations

n = int(input())
graph = [input().split(" ") for _ in range(n)]

empty_spaces = []
teacher_spaces = []
for i in range(n):
    for j in range(n):
        if graph[i][j] == "X":
            empty_spaces.append([i, j])
        if graph[i][j] == "T":
            teacher_spaces.append([i, j])

choices = combinations(empty_spaces, 3)


def find_students(teacher_spaces, temp_graph):
    d_row = [1, -1, 0, 0]
    d_col = [0, 0, 1, -1]
    for teacher_space in teacher_spaces:
        teacher_row, teacher_col = teacher_space
        stop_j_flags = [False] * 4
        for i in range(1, n):
            for j in range(4):
                if stop_j_flags[j]:
                    continue

                next_row = teacher_row + i * d_row[j]
                next_col = teacher_col + i * d_col[j]

                if next_row < 0 or next_row > n - 1 or next_col < 0 or next_col > n - 1:
                    continue
                if temp_graph[next_row][next_col] == "T":
                    stop_j_flags[j] = True
                    continue
                if temp_graph[next_row][next_col] == "O":
                    stop_j_flags[j] = True
                    continue
                if temp_graph[next_row][next_col] == "X":
                    continue
                if temp_graph[next_row][next_col] == "S":
                    return True

    return False


flag = False
for choice in choices:
    temp_graph = deepcopy(graph)
    for obj in choice:
        row, col = obj
        temp_graph[row][col] = "O"
    find_result = find_students(teacher_spaces, temp_graph)
    if not find_result:
        print("YES")
        flag = True
        break
if not flag:
    print("NO")
