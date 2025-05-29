for n in range(4, 10000):
    a = '4' + '2' * n
    while '42' in a or '8222' in a or '2222' in a:
        if '42' in a:
            a = a.replace('42', '2', 1)
        if '8222' in a:
            a = a.replace('8222', '24', 1)
        if '2222' in a:
            a = a.replace('2222', '8', 1)
    sdigits = sum([int(x) for x in a])
    if sdigits == 110:
        print(n)