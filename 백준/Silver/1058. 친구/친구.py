# 그래프로 될거같지만 플로이드워셜을 배웟으니 그걸로
# 시간복잡도 n^3
# 
n = int(input())
friend = []

for i in range(n):
    friend.append(list(input()))

def floyd(n):
    connectlist = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if(j == k):
                    continue
                if(friend[j][k] == 'Y' or (friend[i][k] == 'Y' and friend[j][i] == 'Y')):
                    connectlist[j][k] = 1
    ans = 0
    for i in connectlist:
        ans = max(ans, sum(i))
    
    return ans

print(floyd(n))
