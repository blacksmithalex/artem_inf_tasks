alp = '0123456789ABCDEFGH'
for x in alp:
    l1 = int(f'98897{x}21', 19)
    l2 = int(f'2{x}923', 19)
    v = l1 + l2
    if v % 18 == 0:
        s = v // 18
        print(s)