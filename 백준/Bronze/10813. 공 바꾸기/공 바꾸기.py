n, m = list(map(int, input().split()))
li = []
for i in range(1, n+1):
    li.append(i)
for _ in range(m):
    i, j = list(map(int, input().split()))
    li[i-1], li[j-1] = li[j-1], li[i-1]

for o in range(n):
    print(li[o], end = " ")