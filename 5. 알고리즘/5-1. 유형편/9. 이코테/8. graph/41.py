def find_parent(parent_table, x):
    if parent_table[x] != x:
        parent_table[x] = find_parent(parent_table, parent_table[x])
    return parent_table[x]


def union_parent(parent_table, a, b):
    root_a = find_parent(parent_table, a)
    root_b = find_parent(parent_table, b)
    if root_a < root_b:
        parent_table[root_b] = root_a
    else:
        parent_table[root_b] = root_a


n, m = map(int, input().split(" "))
parent_table = [i for i in range(0, n + 1)]
edges = []
for row in range(1, n + 1):
    line = list(map(int, input().split(" ")))
    for col in range(1, n + 1):
        if row < col:
            continue
        if line[col - 1] == 1:
            edges.append([row, col])
plan = list(map(int, input().split(" ")))
plan = list(set(plan))

for edge in edges:
    a, b = edge
    if find_parent(parent_table, a) != find_parent(parent_table, b):
        union_parent(parent_table, a, b)

flag = True
root = parent_table[plan[0]]
for city in plan:
    if root != parent_table[city]:
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
