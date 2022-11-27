def sort_dict(dict):
    for key in dict:
        dict[key].sort()


def binary_search(data, start, end, target):
    if start > end:
        return -1

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search(data, mid + 1, end, target)
    elif data[mid] > target:
        return binary_search(data, start, mid - 1, target)


def solution(info, query):
    language = {
        'java': [],
        'python': [],
        'cpp': [],
    }
    major = {
        'frontend': [],
        'backend': [],
    }
    resume = {
        'junior': [],
        'senior': [],
    }
    food = {
        'pizza': [],
        'chicken': [],
    }
    total = []

    for i in range(len(info)):
        info_list = info[i].split(" ")
        language[info_list[0]].append(i)
        major[info_list[1]].append(i)
        resume[info_list[2]].append(i)
        food[info_list[3]].append(i)
        total.append(info_list)

    sort_dict(language)
    sort_dict(major)
    sort_dict(resume)
    sort_dict(food)

    results = []
    for j in range(len(query)):
        query_list = query[j].split(" ")
        selectors = list(range(len(info)))
        if query_list[0] != "-":
            selectors = language[query_list[0]]
        if query_list[2] != "-":
            i = 0
            while i < len(selectors):
                selector = selectors[i]
                if binary_search(major[query_list[2]], 0, len(major[query_list[2]]) - 1, selector) == -1:
                    del selectors[i]
                    i -= 1
                i += 1
        if query_list[4] != "-":
            i = 0
            while i < len(selectors):
                selector = selectors[i]
                if binary_search(resume[query_list[4]], 0, len(resume[query_list[4]]) - 1, selector) == -1:
                    del selectors[i]
                    i -= 1
                i += 1
        if query_list[6] != "-":
            i = 0
            while i < len(selectors):
                selector = selectors[i]
                if binary_search(food[query_list[6]], 0, len(food[query_list[6]]) - 1, selector) == -1:
                    del selectors[i]
                    i -= 1
                i += 1

        result = []
        for selector in selectors:
            if int(total[selector][4]) >= int(query_list[7]):
                result.append(selector)
        results.append(len(result))
    print(results)
    return results