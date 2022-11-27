import re
from functools import cmp_to_key


def str_reverse(s):
    result = ""
    for char in reversed(s):
        result += char

    return result


def binary_first_search(data, start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if len(data[mid]) == target:
        if mid == 0:
            return mid
        elif len(data[mid - 1]) == target:
            return binary_first_search(data, start, mid - 1, target)
        else:
            return mid
    elif len(data[mid]) < target:
        return binary_first_search(data, mid + 1, end, target)
    else:
        return binary_first_search(data, start, mid - 1, target)


def binary_last_search(data, start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if len(data[mid]) == target:
        if mid == len(data) - 1:
            return mid
        elif len(data[mid + 1]) == target:
            return binary_last_search(data, mid + 1, end, target)
        else:
            return mid
    elif len(data[mid]) < target:
        return binary_last_search(data, mid + 1, end, target)
    else:
        return binary_last_search(data, start, mid - 1, target)


def binary_first_question_search(data, start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if data[mid] == target:
        if mid == 0:
            return mid
        elif data[mid - 1] == target:
            return binary_first_question_search(data, start, mid - 1, target)
        else:
            return mid
    else:
        return binary_first_question_search(data, mid + 1, end, target)


def binary_last_question_search(data, start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if data[mid] == target:
        if mid == len(data) - 1:
            return mid
        elif data[mid + 1] == target:
            return binary_last_question_search(data, mid + 1, end, target)
        else:
            return mid
    else:
        return binary_last_question_search(data, start, mid - 1, target)


def binary_first_pattern_search(data, start, end, target, mode):
    if start > end:
        return -1

    mid = (start + end) // 2
    pattern = f"^{target}" if mode == "front" else f"{target}$"
    if len(re.findall(pattern, data[mid])) == 1:
        if mid == 0:
            return mid
        elif len(re.findall(pattern, data[mid - 1])) == 1:
            return binary_first_pattern_search(data, start, mid - 1, target, mode)
        else:
            return mid
    if mode == "front":
        if data[mid] < target:
            return binary_first_pattern_search(data, mid + 1, end, target, mode)
        elif data[mid] > target:
            return binary_first_pattern_search(data, start, mid - 1, target, mode)
    else:
        if str_reverse(data[mid]) < str_reverse(target):
            return binary_first_pattern_search(data, mid + 1, end, target, mode)
        elif str_reverse(data[mid]) > str_reverse(target):
            return binary_first_pattern_search(data, start, mid - 1, target, mode)


def binary_last_pattern_search(data, start, end, target, mode):
    if start > end:
        return -1

    mid = (start + end) // 2

    pattern = f"^{target}" if mode == "front" else f"{target}$"
    if len(re.findall(pattern, data[mid])) == 1:
        if mid == len(data) - 1:
            return mid
        elif len(re.findall(pattern, data[mid + 1])) == 1:
            return binary_last_pattern_search(data, mid + 1, end, target, mode)
        else:
            return mid
    if mode == "front":
        if data[mid] < target:
            return binary_last_pattern_search(data, mid + 1, end, target, mode)
        elif data[mid] > target:
            return binary_last_pattern_search(data, start, mid - 1, target, mode)
    else:
        if str_reverse(data[mid]) < str_reverse(target):
            return binary_last_pattern_search(data, mid + 1, end, target, mode)
        elif str_reverse(data[mid]) > str_reverse(target):
            return binary_last_pattern_search(data, start, mid - 1, target, mode)


def compare_func(a, b):
    for i in reversed(range(len(a))):
        if a[i] != b[i]:
            return ord(a[i]) - ord(b[i])


def solution(words, queries):
    words = sorted(words, key=lambda x: len(x))
    sorted_words = sorted(words, key=lambda x: x)
    results = []
    for query in queries:
        if query[0] == "?" and query[-1] == "?":
            first_index = binary_first_search(sorted_words, 0, len(sorted_words) - 1, len(query))
            if first_index == -1:
                results.append(0)
                continue
            last_index = binary_last_search(sorted_words, 0, len(sorted_words) - 1, len(query))
            results.append(last_index - first_index + 1)
        elif query[-1] == "?":
            first_index = binary_first_search(sorted_words, 0, len(sorted_words) - 1, len(query))
            if first_index == -1:
                results.append(0)
                continue
            last_index = binary_last_search(sorted_words, 0, len(sorted_words) - 1, len(query))
            index = binary_first_question_search(query, 0, len(query) - 1, "?")
            pattern = f"{query[0:index]}"
            filtered_words = sorted_words[first_index:last_index + 1]
            final_first_index = binary_first_pattern_search(filtered_words, 0, len(filtered_words) - 1, pattern,
                                                            mode="front")
            if final_first_index == -1:
                results.append(0)
                continue
            final_last_index = binary_last_pattern_search(filtered_words, 0, len(filtered_words) - 1, pattern,
                                                          mode="front")
            results.append(final_last_index - final_first_index + 1)
        elif query[0] == "?":
            first_index = binary_first_search(words, 0, len(words) - 1, len(query))
            if first_index == -1:
                results.append(0)
                continue
            last_index = binary_last_search(words, 0, len(words) - 1, len(query))

            index = binary_last_question_search(query, 0, len(query) - 1, "?")
            pattern = f"{query[index + 1:len(query)]}"
            filtered_words = words[first_index:last_index + 1]
            filtered_words.sort(key=cmp_to_key(compare_func))
            final_first_index = binary_first_pattern_search(filtered_words, 0, len(filtered_words) - 1, pattern,
                                                            mode="back")
            if final_first_index == -1:
                results.append(0)
                continue
            final_last_index = binary_last_pattern_search(filtered_words, 0, len(filtered_words) - 1, pattern,
                                                          mode="back")
            results.append(final_last_index - final_first_index + 1)

    print(results)
    return results


solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],
         ["????o"])
