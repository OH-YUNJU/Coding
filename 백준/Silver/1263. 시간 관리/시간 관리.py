import sys

N = int(input())

li = []
for _ in range(N):
    T, S = map(int, sys.stdin.readline().split())
    li.append((S, T))
    
li.sort(reverse=True)
ans = li[0][0] - li[0][1]

for i in range(1, N):
    if ans > li[i][0]:
        ans = li[i][0] - li[i][1]
    else:
        ans -= li[i][1]
if ans < 0:
    ans = -1
    
print(ans)
