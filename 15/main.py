#O(N)
file = open('27_B_9794.txt')
K = int(file.readline())
N = int(file.readline())
a = [int(x) for x in file]
file.close()
count = 0

l, r = 0, len(a) - 1
while l < r:
    if a[l] + a[r] >= K:
        count += r - l
        r -= 1
    else:
        l += 1
print(count)