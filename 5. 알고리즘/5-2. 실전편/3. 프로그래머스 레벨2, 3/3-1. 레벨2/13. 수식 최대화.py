from copy import deepcopy
from itertools import permutations


def solution(expression):
    symbols = ["+", "-", "*"]
    expression_list = []
    number = ""
    for char in expression:
        if char not in symbols:
            number += char
        else:
            expression_list.append(int(number))
            expression_list.append(char)
            number = ""
    expression_list.append(number)

    iterator = permutations(symbols, 3)

    max_value = 0
    for permutation in iterator:
        copy_expression_list = deepcopy(expression_list)
        for symbol in permutation:
            while True:
                try:
                    index = copy_expression_list.index(symbol)
                    copy_expression_list[index - 1] = eval(
                        f"{copy_expression_list[index - 1]}{symbol}{copy_expression_list[index + 1]}")
                    del copy_expression_list[index]
                    del copy_expression_list[index]
                except Exception as e:
                    break
        if max_value < abs(copy_expression_list[0]):
            max_value = abs(copy_expression_list[0])

    return max_value


solution("100-200*300-500+20")
