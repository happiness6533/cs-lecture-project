def dfs(graph, sign_memo, sum_memo, current_node_index, results):
    if sign_memo == "+":
        sum_memo += graph[current_node_index]
    else:
        sum_memo -= graph[current_node_index]
    if current_node_index == len(graph) - 1:
        results.append(sum_memo)
        return
    for next_sign_memo in ["+", "-"]:
        current_node_index += 1
        dfs(graph, next_sign_memo, sum_memo, current_node_index, results)
        current_node_index -= 1


def solution(numbers, target):
    answer = 0
    results = []
    dfs(numbers, "+", 0, 0, results)
    dfs(numbers, "-", 0, 0, results)
    for result in results:
        if result == target:
            answer += 1
    return answer


solution([1, 1, 1, 1, 1], 3)
solution([4, 1, 2, 1], 4)
