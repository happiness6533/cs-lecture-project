from copy import deepcopy

# 상 하 좌 우
d_row = [-1, 1, 0, 0]
d_col = [0, 0, -1, 1]


def show_graph(graph):
    print()
    for i in range(len(graph)):
        print(graph[i])
    print()


def check_end_game(graph, current_node, other_node):
    if graph[current_node[0]][current_node[1]] == 0:
        return True
    last_way = False
    for i in range(len(d_row)):
        next_node_row = current_node[0] + d_row[i]
        next_node_col = current_node[1] + d_col[i]
        if next_node_row < 0 or next_node_col < 0 or next_node_row > len(graph) - 1 or next_node_col > len(
                graph[0]) - 1:
            continue
        if graph[next_node_row][next_node_col] == 0:
            continue
        if next_node_row == other_node[0] and next_node_col == other_node[1]:
            last_way = True
            all_blocked = True
            for j in range(len(d_row)):
                consider_next_node_row = next_node_row + d_row[j]
                consider_next_node_col = next_node_col + d_col[j]
                if consider_next_node_row < 0 or consider_next_node_col < 0 or consider_next_node_row > len(
                        graph) - 1 or consider_next_node_col > len(
                    graph[0]) - 1:
                    continue
                if consider_next_node_row == current_node[0] and consider_next_node_col == current_node[1]:
                    continue
                if graph[consider_next_node_row][consider_next_node_col] == 0:
                    continue
                all_blocked = False
                break
            # 만약 이 노드 주변이 모두 접근 불가라면 내가 지금 이 턴에 들어가야 승리한다
            # 그렇지 않다면 피할곳이 있는 경우에는 피한다
            # 피할곳이 없다면 게임 종료
            if all_blocked == True:
                return False
            else:
                continue
        return False
    if last_way == True:
        return False
    else:
        return True


def dfs(graph, turn_memo, cnt_memo_a, cnt_memo_b, current_node_a, current_node_b, cnt_list):
    turn_memo = "a" if turn_memo == "b" else "b"  # 턴을 교체하고
    current_node = current_node_a if turn_memo == "a" else current_node_b  # 현재 노드를 결정한다
    other_node = current_node_a if turn_memo == "b" else current_node_b  # 고려할 노드를 결정한다

    # print(turn_memo, current_node, other_node, current_node_a, current_node_b)
    result = check_end_game(graph, current_node, other_node)
    # show_graph(graph)
    # print(result)
    # print()
    if result == True:
        winner = 'a' if turn_memo == 'b' else 'b'
        print(f"{winner}가 승리했습니다")
        print(f"{turn_memo}가 {current_node}에서 더 이상 움직일 수 없습니다. a는 {cnt_memo_a}회, b가 {cnt_memo_b}회 움직였습니다")
        print()
        win_cnt = cnt_memo_a if winner == "a" else cnt_memo_b
        loose_cnt = cnt_memo_b if winner == "a" else cnt_memo_a
        if cnt_list[0] > win_cnt:
            cnt_list[0] = win_cnt
            cnt_list[1] = loose_cnt
        elif cnt_list[0] == win_cnt:
            if cnt_list[1] < loose_cnt:
                cnt_list[1] = loose_cnt
        print(cnt_list)
        return

    for i in range(len(d_row)):
        next_node_row = current_node[0] + d_row[i]
        next_node_col = current_node[1] + d_col[i]
        if next_node_row < 0 or next_node_col < 0 or next_node_row > len(graph) - 1 or next_node_col > len(
                graph[0]) - 1:
            continue
        if graph[next_node_row][next_node_col] == 0:
            continue

        copy_graph = deepcopy(graph)
        copy_graph[current_node[0]][current_node[1]] = 0
        next_node = [next_node_row, next_node_col]
        copy_next_node = deepcopy(next_node)
        if turn_memo == "a":
            dfs(copy_graph, turn_memo, cnt_memo_a + 1, cnt_memo_b, copy_next_node, current_node_b, cnt_list)
        else:
            dfs(copy_graph, turn_memo, cnt_memo_a, cnt_memo_b + 1, current_node_a, copy_next_node, cnt_list)


def solution(board, aloc, bloc):
    # 최소
    min_win_cnt = 1e9
    max_loose_cnt = 0

    cnt_list = [min_win_cnt, max_loose_cnt]
    dfs(board, "b", 0, 0, aloc, bloc, cnt_list)
    print(cnt_list)
    return sum(cnt_list)


solution([[1, 1, 1], [1, 1, 1], [1, 1, 1]], [1, 0], [1, 2])
