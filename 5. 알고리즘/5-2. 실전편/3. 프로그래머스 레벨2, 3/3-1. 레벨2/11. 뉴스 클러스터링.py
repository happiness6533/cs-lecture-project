def solution(str1, str2):
    answer = 0

    i = 0
    set1 = []
    while i < len(str1) - 1:
        element = str1[i: i + 2].lower()
        if element.isalpha():
            set1.append(element)
        i += 1
    set1_set = set(set1)

    i = 0
    set2 = []
    while i < len(str2) - 1:
        element = str2[i: i + 2].lower()
        if element.isalpha():
            set2.append(element)
        i += 1
    set2_set = set(set2)

    intersection = list(set1_set & set2_set)
    union = list(set1_set | set2_set)

    intersection_count = 0
    multiple_intersection = []
    for element in intersection:
        count1 = 0
        for v in set1:
            if element == v:
                count1 += 1
        count2 = 0
        for v in set2:
            if element == v:
                count2 += 1
        min_count = min(count1, count2)
        for _ in range(min_count):
            multiple_intersection.append(element)
        intersection_count += min_count
    print(multiple_intersection, intersection_count)

    union_count = 0
    multiple_uniom = []
    for element in union:
        count1 = 0
        for v in set1:
            if element == v:
                count1 += 1
        count2 = 0
        for v in set2:
            if element == v:
                count2 += 1
        max_count = max(count1, count2)
        for _ in range(max_count):
            multiple_uniom.append(element)
        union_count += max_count
    print(multiple_uniom, union_count)

    if union_count == 0:
        answer = 65536
    else:
        print(intersection_count / union_count)
        answer = int((intersection_count / union_count) * 65536)

    return answer