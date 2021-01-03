import itertools
from typing import List


def solution(numbers: List[int]) -> str:
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)  # ['666', '101010', '222]
    answer = str(int(''.join(numbers)))  # [0, 0, 0, 0] 들어오면 '0000'이 return 되므로 int 변환 후 다시 str 변환
    return answer


print(solution(numbers=[6, 10, 2]))  # return : '6210'
