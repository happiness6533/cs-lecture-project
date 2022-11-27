def solution(numbers):
    str_numbers = list(map(str, numbers))
    str_numbers.sort(reverse=True)
    print(str_numbers)
    return "".join(str_numbers)


solution([6, 13, 10, 2, 20])
# https://programmers.co.kr/learn/courses/30/lessons/42746
