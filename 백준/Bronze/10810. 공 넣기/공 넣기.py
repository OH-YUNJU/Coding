n, m = list(map(int, input().split()))
li = [0] * (n+1)
for _ in range(m):
    i, j, k = list(map(int, input().split()))
    for o in range(i, j+1):
        li[o] = k
for p in range(1, n+1):
    print(li[p], end=" ")