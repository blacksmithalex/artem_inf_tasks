def f(x, A):
    l1 = (x % A == 0)
    l2 = x in range(60, 80 + 1)
    l3 = x % 22 != 0
    return l1 or (l2 <= l3)

for A in range(1, 1000):
    flag = True
    for x in range(1, 1000):
        if not f(x, A):
            flag = False
    if flag:
        print(A)