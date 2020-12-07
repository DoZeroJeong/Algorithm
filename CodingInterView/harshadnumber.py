def harshadNumber(self, number: int) -> bool:
    number_list = list(str(number))
    total_num = 0
    for i in range(len(number_list)):
        total_num += int(number_list[i])
        print(total_num)
    if number % total_num == 0:
        return True
    else:
        return False


print(harshadNumber(self=None, number=10))
