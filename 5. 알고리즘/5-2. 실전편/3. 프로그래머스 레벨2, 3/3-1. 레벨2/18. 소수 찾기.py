def is_sosu(str_number):
    while True:
        if str_number[0] == "0":
            if len(str_number) >= 2:
                str_number = str_number[1:]
            else:
                return -1
        else:
            break

    number = int(str_number)
    print(number)
    if number == 1:
        return -1
    for i in range(2, number):
        if number % i == 0:
            return -1
    return number

from itertools  import permutations
def solution(numbers):
    answer = 0
    answer_list = []
    all_numbers = []
    for count in range(1, len(numbers) + 1):
        all_numbers += list(permutations(list(numbers), count))
    all_numbers = list(set(all_numbers))
    for i in range(len(all_numbers)):
        list_str_number = all_numbers[i]
        str_number = ''
        for j in range(len(list_str_number)):
            str_number += list_str_number[j]
        print(str_number)
        result = is_sosu(str_number)
        if result != -1 and result not in answer_list:
            answer_list.append(result)
    print(answer_list)
    return len(answer_list)