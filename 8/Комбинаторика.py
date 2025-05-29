c=0
for a1 in 'ДГШ':
    for a2 in 'ДГИАШЭ':
        for a3 in 'ДГИАШЭ':
            for a4 in 'ДГИАШЭ':
                for a5 in 'ИАЭ':
                    a=a1+a2+a3+a4+a5
                    c+=1
                    print(c,a)