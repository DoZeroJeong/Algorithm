def sockMerchant(n, ar):
    ar_set = set(ar)
    print('ar_set', ar_set)
    num = 0
    for i in ar_set:
        print('i', i)
        num = num + ar.count(i) // 2
        print('num', num)
    return num