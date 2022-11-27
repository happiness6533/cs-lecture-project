def solution(s):
    answer = []

    s = s[2:-2]
    s = list(map(lambda x: x.split(','), s.split("},{")))
    s.sort(key=lambda x: len(x))
    for i in range(len(s)):
        result = [int(element) for element in s[i] if int(element) not in answer]
        answer += result

    return answer