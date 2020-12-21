from typing import List


def solution(array: List[int], commands: List[List[int]]) -> List[int]:
    answer = []
    for command in commands:
        a = array[command[0]-1:command[1]]
        a.sort()
        answer.append(a[command[2]-1])
    return answer


print(solution(array=[1, 5, 2, 6, 3, 7, 4], commands=[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))  # result = [5, 6, 3]
