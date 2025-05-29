def f(n):
    bn= bin(n)
    bn += str(bn.count('1')%2)
    bn += str(bn.count('1') % 2)
    return int(bn,2)
for n in range(1000):
    if f(n)>253:
        print(n)