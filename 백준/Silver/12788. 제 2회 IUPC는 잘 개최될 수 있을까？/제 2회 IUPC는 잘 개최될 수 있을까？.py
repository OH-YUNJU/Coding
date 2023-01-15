n = int(input())
m, k = map(int, input().split())
li = list(map(int, input().split()))
peo = m*k
ans, pen = 0, 0
li.sort(reverse=True)

for i in range(0, n):
    if(pen < peo):
        pen += li[i]
        ans += 1
    else:
        break

if(pen >= peo):
    print(ans)
else:
    print("STRESS")