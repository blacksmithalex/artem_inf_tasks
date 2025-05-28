def f(a, b):
    if a < b:
        return 0
    elif a == b:
        return 1
    else:
        return f(a - 2, b) + f(a // 2, b)

print(f(32, 14) * f(14, 1))