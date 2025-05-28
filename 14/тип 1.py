def f(n):
    res = []
    while n > 0:
        res.append(n % 25)
        n //= 25
    return res[::-1]

l1 = 3 * 3125 ** 8 + 2 * 625 ** 7 - 4 * 625 ** 6 + 3 * 125 ** 5 - 2 * 25 ** 4 - 2025
v = f(l1)
print(v.count(0))
