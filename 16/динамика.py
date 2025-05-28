F = [0] * 50000
for n in range(20):
    F[n] = n
for n in range(20, 50000):
    F[n] = (n - 6) * F[n - 7]

l1 = (F[47872] - 290 * F[47865]) // F[47858]
print(l1)