n = int(input())
card = [0] + list(map(int, input().split()))
dp = [0 for i in range(10001)]

for i in range(1, n+1): 
    for j in range(1, i+1):
        dp[i] = max(dp[i], card[j] + dp[i-j])

print(dp[n])