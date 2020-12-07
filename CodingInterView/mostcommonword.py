"""

금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며,
구두점(마침표, 쉼표 등) 또한 무시한다.

입력 : paragraph = "Bob hit al ball, the hit BALL flew far after it was hit."
      banned = ["hit"]
출력 : "ball"

"""
import collections
from typing import List
import re


def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
    # 정규식 \w 표현은 문자를 뜻한다. 앞에 ^은 not을 의미한다.
    words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]
    # [word for word in re.sub(r'[^\w]', ' ', paragraph)]는 리스트형태로 저장된다.

    counts = collections.Counter(words)
    return counts.most_common(1)[0][0]


print(mostCommonWord(self=None,
                     paragraph="Bob hit al ball, the hit BALL flew far after it was hit.",
                     banned=["hit"]))
