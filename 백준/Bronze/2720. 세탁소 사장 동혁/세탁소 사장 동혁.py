n = int(input())
div = [25, 10, 5, 1]
for _ in range(n):
    coin = int(input())
    ans = []
    li = coin
    for i in (div):
        ans.append(li // i)
        li = li % i
    print(*ans)
        