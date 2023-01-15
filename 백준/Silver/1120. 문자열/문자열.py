a, b = input().split()
minCnt = 50

for i in range(len(b) - len(a) + 1):
    count = 0
    for j in range(len(a)):
        if b[j+i] != a[j]:
            count += 1
    if count < minCnt:
        minCnt = count
        
print(minCnt)