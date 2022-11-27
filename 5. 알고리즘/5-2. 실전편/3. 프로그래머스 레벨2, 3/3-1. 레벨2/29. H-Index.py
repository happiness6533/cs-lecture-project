def is_h_index_candidate(citations, h):
    h_cnt = 0
    if h == 0:
        return True

    for i in range(len(citations)):
        if citations[i] >= h:
            h_cnt += 1
            if h_cnt == h:
                return True

    return False


def binary_search(start, end, citations):
    if start > end:
        return -1

    mid = (start + end) // 2
    if is_h_index_candidate(citations, mid):
        if mid == len(citations):
            return mid
        if is_h_index_candidate(citations, mid + 1):
            return binary_search(mid + 1, end, citations)
        else:
            return mid
    else:
        return binary_search(start, mid - 1, citations)


def solution(citations):
    answer = binary_search(0, len(citations), citations)
    print(answer)
    return answer


solution([0, 0, 0, 0, 0])
