alp = sorted('ПОБЕДА')
n = 1
for a1 in alp:
    for a2 in alp:
        for a3 in alp:
            for a4 in alp:
                for a5 in alp:
                    for a6 in alp:
                        a = a1 + a2 + a3 + a4 + a5 + a6
                        if n % 2 == 0 and a1 == 'О' and len(set(a)) == 6:
                            print(n, a)
                        n += 1