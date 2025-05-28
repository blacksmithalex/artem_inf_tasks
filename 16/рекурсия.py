from sys import setrecursionlimit
setrecursionlimit(50000)
def f(n):
    if n < 20:
        return n
    else:
        return (n - 6) * f(n - 7)

l1 = (f(47872) - 290 * f(47865)) // f(47858)
print(l1)