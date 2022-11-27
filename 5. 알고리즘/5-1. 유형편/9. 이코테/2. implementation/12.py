from copy import deepcopy


def check_ignore(frame, result):
    if len(result) == 0:
        return False
    temp_result = deepcopy(result)
    temp_result.append([frame[0], frame[1], frame[2]])
    temp_result.sort(key=lambda x: [x[0], x[1], x[2]])
    print(temp_result)
    index = temp_result.index([frame[0], frame[1], frame[2]])
    print(index)
    if frame[2] == 0:  # 기둥
        if (temp_result[index - 1][0] == frame[0] and temp_result[index - 1][1] == frame[1]) or (temp_result[index + 1][0] == frame[0] and temp_result[index + 1][1] == frame[1]):
            result = temp_result
            return


def solution(build_frame):
    result = []
    for i in range(len(build_frame)):
        if build_frame[i][3] == 1:
            ignore = check_ignore(build_frame[i], result)
            if not ignore:
                result.append([build_frame[i][0], build_frame[i][1], build_frame[i][2]])
        else:
            ignore = check_ignore(build_frame[i], result)
            if not ignore:
                result.remove([build_frame[i][0], build_frame[i][1], build_frame[i][2]])

    return result


solution([[0, 0, 0, 1],
          [2, 0, 0, 1],
          [4, 0, 0, 1],
          [0, 1, 1, 1],
          [1, 1, 1, 1],
          [2, 1, 1, 1],
          [3, 1, 1, 1],
          [2, 0, 0, 0],
          [1, 1, 1, 0],
          [2, 2, 0, 1]])
