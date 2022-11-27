def scan_manhattan_range(place, i, j):
    d_row = [0, -1, 0, 1, -2, -1, 0, 1, 2, -1, 0, 1, 0]
    d_col = [-2, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 2]
    find_bad_flag = False
    for k in range(len(d_row)):
        if i + d_row[k] < 0 or i + d_row[k] > 4 or j + d_col[k] < 0 or j + d_col[k] > 4:
            continue
        if place[i + d_row[k]][j + d_col[k]] == "P":
            if abs(d_row[k]) + abs(d_col[k]) == 1:
                find_bad_flag = True
                break
            if abs(d_row[k]) + abs(d_col[k]) == 2:
                if k % 4 == 0:  # 일직선
                    if place[(i + i + d_row[k]) // 2][(j + j + d_col[k]) // 2] != "X":
                        find_bad_flag = True
                        break
                else:  # 대각선
                    if place[i][j + d_col[k]] != "X" or place[i + d_row[k]][j] != "X":
                        find_bad_flag = True
                        break
    return find_bad_flag


def solution(places):
    answer = []
    for place in places:
        find_bad_flag = False
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    # 1. 주변에 맨하탄 거리 내부 스캔
                    # 2. 거리가 1이면 무조건 위반
                    # 3. 거리가 2라면 사이에 테이블 있는지 스캔
                    if scan_manhattan_range(place, i, j):
                        find_bad_flag = True
                        break
            if find_bad_flag:
                break
        if find_bad_flag:
            answer.append(0)
        else:
            answer.append(1)

    return answer