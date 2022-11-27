from copy import deepcopy


def rotate90(key):
    # 0,0 => 0,2
    # 1,0 => 0,1
    # 2,0 => 0,0
    key_len = len(key)
    new_key = [[0] * key_len for _ in range(key_len)]
    for row in range(key_len):
        for col in range(key_len):
            new_key[col][key_len - 1 - row] = key[row][col]

    return new_key


def rotate180(key):
    key_len = len(key)
    new_key = [[0] * key_len for _ in range(key_len)]
    for row in range(key_len):
        for col in range(key_len):
            new_key[key_len - 1 - row][key_len - 1 - col] = key[row][col]
    return new_key


def rotate270(key):
    key_len = len(key)
    new_key = [[0] * key_len for _ in range(key_len)]
    for row in range(key_len):
        for col in range(key_len):
            new_key[key_len - 1 - col][row] = key[row][col]
    return new_key


def rotate_all(key):
    return [key, rotate90(key), rotate180(key), rotate270(key)]


def padding(lock, key_size):
    padding_lock = [[0] * (key_size * 2 + len(lock)) for _ in range(key_size * 2 + len(lock))]
    for i in range(key_size, key_size + len(lock)):
        for j in range(key_size, key_size + len(lock)):
            padding_lock[i][j] = lock[i - key_size][j - key_size]

    return padding_lock


def make_combination(i, j, key, temp_padding_lock):
    for k in range(len(key)):
        for l in range(len(key)):
            temp_padding_lock[i + k][j + l] += key[k][l]


def move(key, lock, padding_lock):
    for i in range(0, len(key) + len(lock) ):
        for j in range(0, len(key) + len(lock) ):
            temp_padding_lock = deepcopy(padding_lock)
            make_combination(i, j, key, temp_padding_lock)

            result = True
            for k in range(len(lock)):
                for l in range(len(lock)):
                    if temp_padding_lock[len(key) + k][len(key) + l] != 1:
                        result = False
                        break
                if not result:
                    break

            if result:
                # for x in range(len(key)):
                #     print(key[x])
                # print(i, j)
                # for x in range(len(temp_padding_lock)):
                #     print(temp_padding_lock[x])
                # print()
                return result

    return False


def solution(key, lock):
    answer = False

    # 회전
    rotate_results = rotate_all(key)

    # 패딩
    padding_lock = padding(lock, len(key))

    # 이동
    for rotate_result in rotate_results:
        answer = move(rotate_result, lock, padding_lock)
        # print(answer, rotate_result, lock, padding_lock,)
        if answer:
            return answer

    return answer