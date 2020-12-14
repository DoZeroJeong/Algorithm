from typing import List


def solution(prices: List[int]) -> List[int]:
    price_list = list()
    for i in range(len(prices)-1):
        time = 0
        for j in range(i+1, len(prices)):
            time += 1
            if prices[i] > prices[j]:  # 처음 구매한가격이 나중보다 낮을 경우 break
                break
        price_list.append(time)
    price_list += [0]  # 마지막 가격은 진행이 안되기때문에 0 입력
    return price_list


print(solution(prices=[1, 2, 3, 2, 4]))
