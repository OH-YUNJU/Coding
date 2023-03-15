n = int(input())
li = list(map(int, input().split()))
reli = li[::-1]
updp = [1 for i in range(n)]
dodp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if(li[i] > li[j]):
            updp[i] = max(updp[i], updp[j]+1)
        if(reli[i] > reli[j]):
            dodp[i] = max(dodp[i], dodp[j]+1)

ans = [0 for i in range(n)]
for i in range(n):
    ans[i] = updp[i] + dodp[n-i-1] - 1

print(max(ans))