n, q = map(int, input().split())
money = [0 for _ in range(n+1)]

for _ in range(q):
    tmp, p, x = map(int, input().split())
    if(tmp == 1):
        money[p] += x
    else:
        print(sum(money[p:x+1]))
        