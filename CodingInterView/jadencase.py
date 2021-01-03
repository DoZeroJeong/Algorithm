def solution(s: str) -> str:
    s.lower()
    s_list = s.split(' ')
    anwser = ''
    for s in s_list:
        s = s.capitalize()
        anwser += s+' '
    return anwser[:-1]


print(solution(s="for the last week"))
