import itertools


def calc_all(arr1, arr2):
    result = []
    for i in range(len(arr1) - 1):
        for j in range(len(arr2) - 1):
            result.append(arr1[i] + arr2[j])
            result.append(arr1[i] - arr2[j])
            result.append(arr2[j] - arr1[i])
            result.append(arr1[i] * arr2[j])
            if arr2[j] != 0:
                result.append(arr1[i] // arr2[j])
            if arr1[i] != 0:
                result.append(arr2[j] // arr1[i])
    for i in range(len(arr2)):
        result.append(arr1[-1] + arr2[i])
        result.append(arr1[-1] - arr2[i])
        result.append(arr2[i] - arr1[-1])
        result.append(arr1[-1] * arr2[i])
        if arr2[i] != 0:
            result.append(arr1[-1] // arr2[i])
        result.append(arr2[i] // arr1[-1])
    for i in range(len(arr1)):
        result.append(arr2[-1] + arr1[i])
        result.append(arr2[-1] - arr1[i])
        result.append(arr2[-1] * arr1[i])
        if arr1[i] != 0:
            result.append(arr2[-1] // arr1[i])
        result.append(arr1[i] // arr2[-1])

    result = list(set(result))
    result.append(int(str(arr1[-1]) + str(arr2[-1])))

    return result


def solution(N, number):
    if N == number:
        return 1

    count = 1
    calc_numbers = [None, [N]]
    while True:
        next_calc_numbers = []
        for j in range(1, (count + 1) // 2 + 1):
            next_calc_numbers.append(calc_all(calc_numbers[j], calc_numbers[count + 1 - j]))
        next_calc_numbers = list(itertools.chain.from_iterable(next_calc_numbers))
        calc_numbers.append(next_calc_numbers)
        count += 1

        if number in next_calc_numbers:
            return count
        if count >= 8:
            return -1

# 다이나믹 프로그래밍
solution(5, 12)
