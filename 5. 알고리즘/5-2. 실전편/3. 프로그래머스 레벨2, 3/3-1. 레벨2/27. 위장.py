from itertools import combinations


def solution(clothes):
    clothes_dict = {}
    for clothe in clothes:
        if clothe[1] not in clothes_dict.keys():
            clothes_dict[clothe[1]] = [clothe[0]]
        else:
            clothes_dict[clothe[1]].append(clothe[0])

    answer = 1
    for key in clothes_dict.keys():
        answer *= len(clothes_dict[key]) + 1

    answer -= 1
    print(answer)
    return answer


solution([["crowmask", "face"], ["bluesunglasses", "face"], ["smoky_makeup", "face"]])
# https://programmers.co.kr/learn/courses/30/lessons/42578
