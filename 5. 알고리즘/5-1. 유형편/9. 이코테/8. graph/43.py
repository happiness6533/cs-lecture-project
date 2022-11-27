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
costs = []
all_cost = 0
for _ in range(m):
    x, y, z = map(int, input().split(" "))
    edges.append([z, x, y])
    all_cost += z

edges.sort()
for edge in edges:
    cost, a, b = edge
    if find_parent(parent_table, a) != find_parent(parent_table, b):
        union_parent(parent_table, a, b)
        costs.append(cost)

costs.sort()
print(all_cost - sum(costs))
