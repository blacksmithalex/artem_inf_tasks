from math import ceil
#x (бит) - глубина кодирования, то есть количество бит на каждый символ
for x in range(1, 100):
    one_memory = ceil(119 * x / 8) #размер одного серийного номера в байтах
    if 125_300 * one_memory > 23 * 1024 * 1024:
        print(x)
        break
#x = 13 - минимальная глубина кодирования, удовлетворяющая условию
print(f'Ответ = {2**12 + 1}')
