n = int(input())
sum = [0] * 100001
num = list(map(int, input().split()))

for i in range(1, n+1):
    sum[i] = sum[i-1] + num[i-1]

m = int(input())

for i in range(m):
    l, k = map(int, input().split())
    print(sum[k+1] - sum[l])