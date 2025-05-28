#19
def f(x, p):
    if x >= 128 and p == 3:
        return True
    if x < 128 and p == 3:
        return False
    if x >= 128:
        return False
    else:
        if p % 2 == 0:
            return f(x + 2, p + 1) or f(x + 5, p + 1) or f(x * 2, p + 1)
        else:
            return f(x + 2, p + 1) and f(x + 5, p + 1) and f(x * 2, p + 1)

for s in range(2, 127 + 1):
    if f(s, 1):
        print(s)

#20
def f(x, p):
    if x >= 128 and p == 4:
        return True
    if x < 128 and p == 4:
        return False
    if x >= 128:
        return False
    else:
        if p % 2 == 1:
            return f(x + 2, p + 1) or f(x + 5, p + 1) or f(x * 2, p + 1)
        else:
            return f(x + 2, p + 1) and f(x + 5, p + 1) and f(x * 2, p + 1)

for s in range(2, 127 + 1):
    if f(s, 1):
        print(s)

#21
def f(x, p):
    if x >= 128 and (p == 5 or p == 3):
        return True
    if x < 128 and p == 5:
        return False
    if x >= 128:
        return False
    else:
        if p % 2 == 0:
            return f(x + 2, p + 1) or f(x + 5, p + 1) or f(x * 2, p + 1)
        else:
            return f(x + 2, p + 1) and f(x + 5, p + 1) and f(x * 2, p + 1)

for s in range(2, 127 + 1):
    if f(s, 1):
        print(s)