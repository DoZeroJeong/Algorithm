def reverse(x: int) -> int:
    a = 0
    if x > 0:
        a = int(str(x)[::-1])
        if a < 2 ** 31:
            return a
        else:
            return 0
    elif x <= 0:
        a = -1 * int(str(x * -1)[::-1])
        if a >= -2 ** 31:
            return a
        else:
            return 0


print(reverse(x=123))
print(reverse(x=-123))
print(reverse(x=0))
