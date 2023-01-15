n, m = map(int, input().split())
h = []

for i in range(n):
    h.append(list(map(int, input().split())))
for i in range(n):
    res = list(map(int, input().split()))
    for j in range(m):
        h[i][j] += res[j]

for i in range(n):
    for j in range(m):
        print(h[i][j], end = " ")
    print()