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
        parent_table[root_a] = root_b


n, m = map(int, input().split(' '))
parent_table = [i for i in range(0, n + 1)]
for _ in range(m):
    menu, a, b = map(int, input().split(' '))
    if menu == 0:
        union_parent(parent_table, a, b)
    else:
        print("YES") if parent_table[a] == parent_table[b] else print("NO")
