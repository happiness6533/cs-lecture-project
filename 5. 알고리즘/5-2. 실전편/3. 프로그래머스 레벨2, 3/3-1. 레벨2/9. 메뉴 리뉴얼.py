from itertools import combinations


def solution(orders, course):
    answer = []

    for course_len in course:
        orders_by_len = []
        for order in orders:
            for comb in combinations(order, course_len):
                orders_by_len.append(sorted(comb))
        orders_by_len.sort()
        i = 0
        count = 1
        result = []
        max_count = 0
        while i <= len(orders_by_len) - 2:
            if orders_by_len[i] == orders_by_len[i + 1]:
                count += 1
                if i == len(orders_by_len) - 2 and count > 1:
                    if max_count == count:
                        str = ''
                        for char in orders_by_len[i]:
                            str += char
                        result.append(str)
                    elif max_count < count:
                        result = []
                        str = ''
                        for char in orders_by_len[i]:
                            str += char
                        result.append(str)
                        max_count = count
            else:
                if count > 1:
                    if max_count == count:
                        str = ''
                        for char in orders_by_len[i]:
                            str += char
                        result.append(str)
                    elif max_count < count:
                        result = []
                        str = ''
                        for char in orders_by_len[i]:
                            str += char
                        result.append(str)
                        max_count = count
                count = 1
            i += 1
        answer += result
    answer.sort()

    return answer