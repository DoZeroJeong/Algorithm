from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    h = dict()
    for index, value in enumerate(nums):
        n = target - value
        if n not in h:
            h[value] = index
        else:
            return [h[n], index]


print(twoSum(nums=[2, 7, 11, 15], target=9))
print(twoSum(nums=[3, 2, 4], target=6))
