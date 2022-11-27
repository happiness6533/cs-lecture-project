n = int(input())
numbers = list(map(int, input().split(" ")))
operations = list(map(int, input().split(" ")))

# n - 1개의 오퍼레이션 노드 => n으로
visited = [-1] * (n)
graph = [[] for _ in range(n)]
operation_array = [None]
for i in range(4):
    for j in range(operations[i]):
        operation_array.append(i)  # 0=더하기 1=빼기 2=곱하기 3=나누기
for i in range(1, n):
    for j in range(i + 1, n):
        graph[i].append(j)

total_numbers = []


def dfs(graph, start_node, visited, number_index, total_number):
    if number_index == n:
        return

    operation = operation_array[number_index]
    if operation == 0:
        total_number += numbers[number_index]
    elif operation == 1:
        total_number -= numbers[number_index]
    elif operation == 2:
        total_number *= numbers[number_index]
    elif operation == 3:
        if total_number < 0:
            total_number = -((-total_number) // numbers[number_index])
        else:
            total_number //= numbers[number_index]
    total_numbers.append(total_number)

    visited[start_node] = 1
    for next_node in graph[start_node]:
        if visited[next_node] == 1:
            continue
        number_index += 1
        dfs(graph, next_node, visited, number_index, total_number)


visited[0] = 1
for i in range(1, len(operation_array)):
    dfs(graph, i, visited, 1, numbers[0])
    print(total_numbers)
    visited = [-1] * (n)
    visited[0] = 1
