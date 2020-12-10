from typing import List
from itertools import combinations


def solution(nums: List[int]) -> int:

    num_list = list(combinations(nums, 3))
    result = 0
    for num in num_list:
        total_num = 0
        for i in range(0, len(num)):
            total_num = num[i] + total_num
        decimal_check = 0
        for i in range(2, total_num):
            if total_num % i == 0:
                decimal_check = 1
        if decimal_check == 0:
            result += 1
    return result


print(solution(nums=[1, 2, 3, 7, 10, 12]))
