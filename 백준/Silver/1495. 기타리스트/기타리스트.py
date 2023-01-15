n, s, m = list(map(int, input().split()))
vol = list(map(int, input().split()))

dp = [[0] * 1010 for i in range(1010)]
dp[0][s] = 1

for i in range(n):
    for j in range(m+1):
        if dp[i][j] == 1:
            plus = j + vol[i]
            minus = j - vol[i]
           
            if 0 <= plus <= m:
                dp[i+1][plus] = 1
           
            if 0 <= minus <= m:
                dp[i+1][minus] = 1
ans = -1

for i in range(m+1):   
    if dp[n][i] == 1:
        ans = i

print(ans)



