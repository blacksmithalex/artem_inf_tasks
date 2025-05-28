def f(n):
    res = ''
    while n > 0:
        res += str(n % 7)
        n //= 7
    return res[::-1]

for x in range(1, 2030 + 1):
    l1 = f(7 ** 170 + 7 ** 100 - x)
    if l1.count('0') == 71:
        print(x)