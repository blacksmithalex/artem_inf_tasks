def f(a, b):
    if a > b or a == 8:
        return 0
    elif a == b:
        return 1
    else:
        return f(a + 1, b) + f(a + 2, b) + f(a * 2, b)

print(f(3, 14) * f(14, 18))

