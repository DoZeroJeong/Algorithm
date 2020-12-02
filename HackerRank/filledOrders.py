def filledOrders(order, k):
    total = 0
    cont = 0
    order.sort()
    for num in order:
        total = total + num
        if total <= k:
            cont = cont + 1
        else:
            pass
    return cont
