def f(x, y, A):
    return (5 < y) or (x > 32) or (x + 2*y < A)

for A in range(300):
    flag = True
    for x in range(300):
        for y in range(300):
            if not f(x, y, A):
                flag = False
    if flag:
        print(A)