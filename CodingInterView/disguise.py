from typing import List
import collections


def solution(self, clothes: List[List[str]]) -> int:
    result = 1
    clothes_dict = collections.defaultdict(list)
    for clothes in clothes:
        clothes_dict[clothes[1]].append(clothes[0])

    for key in clothes_dict.keys():
        result = result * (len(clothes_dict[key]) + 1)

    return result - 1


print(solution(
    self=None,
    clothes=[['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
))

