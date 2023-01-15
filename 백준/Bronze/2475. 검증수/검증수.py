n = list(map(int, input().split()))

ans = 0
for i in n:
    ans += i**2

print(ans%10)

