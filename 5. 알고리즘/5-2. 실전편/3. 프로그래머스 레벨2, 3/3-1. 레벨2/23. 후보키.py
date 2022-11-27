from itertools import combinations

def is_unique_combination(combination, relation):
    cols = []
    for i in combination:
        col = relation[:][i]

    print(cols)



def solution(relation):
    for i in range(1, len(relation[0]) + 1):
        iterator = combinations(list(range(len(relation[0]))), i)
        for combination in iterator:
            is_unique_combination(combination, relation)



solution([["100", "ryan", "music", "2"],
          ["200", "apeach", "math", "2"],
          ["300", "tube", "computer", "3"],
          ["400", "con", "computer", "4"],
          ["500", "muzi", "music", "3"],
          ["600", "apeach", "music", "2"]])
# https://programmers.co.kr/learn/courses/30/lessons/42890
