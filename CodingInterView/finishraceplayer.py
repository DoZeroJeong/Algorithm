from typing import List
import collections


def solution(participant: List[str], completion: List[str]) -> str:
    participant.sort()
    completion.sort()
    player = collections.Counter(participant) - collections.Counter(completion)

    return list(player)[0]


print(solution(participant=['leo', 'kiki', 'eden'], completion=['eden', 'kiki']))
