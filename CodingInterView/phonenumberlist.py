from typing import List


def solution(phone_book: List[str]) -> bool:
    phone_book.sort()  # 접두어가 0일 경우를 대비해 sort()함수 사용
    for i in range(1, len(phone_book)):
        if phone_book[0] == phone_book[i][0:len(phone_book[0])]:
            return False
    return True


print(solution(['119', '97674223', '1195524421']))
print(solution(	["123", "456", "789"]))
