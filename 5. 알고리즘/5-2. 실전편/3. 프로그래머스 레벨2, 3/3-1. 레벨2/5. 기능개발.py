import math


def solution(progresses, speeds):
    answer = []

    max_value = math.ceil((100 - progresses[0]) / speeds[0])
    count = 1
    for i in range(1, len(progresses)):
        new_max_value = math.ceil((100 - progresses[i]) / speeds[i])
        if new_max_value > max_value:
            max_value = new_max_value
            answer.append(count)
            count = 1
            continue
        count += 1
    answer.append(count)

    return answer


solution([93, 30, 55], [1, 30, 5])
