from typing import List


"""
문제 : 로그를 재정렬하라. 기준은 다음과 같다.

1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

입력 : ['dig1 8 1 4 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']
출력 : ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 4 1', 'dig2 3 6']
"""

logs = ['dig1 8 1 4 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']


def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []  # 문자와 숫자를 구분
    for log in logs:
        if log.split()[1].isdigit():  # 숫자인지 확인
            digits.append(log)
        else:  # 그렇지 않으면 letters 추가
            letters.append(log)

    # 2개의 키를 람다표현식으로 정렬
    # 식별자를 제외한 문자열 [1:]을 키로 하여 정렬하며 동일한 경우 후순위로 식별자 [0]을 지정해 정렬되도록 한다.
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))

    return letters + digits  # 모두 이어 붙여서 리턴


print(reorderLogFiles(self=None, logs=logs))
