def check_diff_char_count(word1, word2):
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count


from collections import deque


def bfs(graph, visited, start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = 0
    while queue:
        current_node = queue.popleft();
        for next_node in graph[current_node]:
            if visited[next_node] != -1:
                continue
            queue.append(next_node)
            visited[next_node] = visited[current_node] + 1


def solution(begin, target, words):
    answer = 0

    graph = {}
    visited = {}

    graph[begin] = []
    visited[begin] = -1
    for i in range(len(words)):
        diff_count = check_diff_char_count(begin, words[i])
        if diff_count == 1:
            graph[begin].append(words[i])

    for word in words:
        graph[word] = []
        visited[word] = -1
        for i in range(len(words)):
            diff_count = check_diff_char_count(word, words[i])
            if diff_count == 1:
                graph[word].append(words[i])

    if target not in words:
        return 0
    bfs(graph, visited, begin)
    print(graph)
    print(visited)
    return visited[target]