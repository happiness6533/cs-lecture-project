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


def get_distance(a, b):
    return min(abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2]))


n = int(input())
coords = []
for i in range(n):
    x, y, z = map(int, input().split(' '))
    coords.append([x, y, z])

parent_table = [i for i in range(0, n + 1)]
edges = []
costs = []

# 01 02 03 04 / 12 "13" 14 / ...
# "13" => "i-1 ~ i" + "i-1 ~ 3"
for i in range(n):
    for j in range(i, n):
        if i == j:
            continue
        cost = get_distance(coords[i], coords[j])
        edges.append([cost, i, j])

    edges.sort()
    for edge in edges:
        cost, a, b = edge
        if find_parent(parent_table, a) != find_parent(parent_table, b):
            union_parent(parent_table, a, b)
            costs.append(cost)
    print(parent_table)
    costs.sort()
    print(sum(costs))
