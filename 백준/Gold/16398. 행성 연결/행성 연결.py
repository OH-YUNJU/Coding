# 크루스칼
# 시간복잡도 nlogn
# 31120kb 52ms
import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    li.append(list(map(int, input().split())))
s = list(i for i in range(n))
money = []
count = 0
idx = 0
answer = 0

for i in range(n):
    for j in range(i+1, n):
        money.append([li[i][j], i, j]) #돈이랑 번호
money.sort()

def find(x):
    if(x != s[x]):
        s[x] = find(s[x])
    return s[x]

def union(x, y):
    s[find(x)] = find(y)

while(count != n-1):
    x = money[idx][1]
    y = money[idx][2]

    if(find(x) != find(y)):
        union(x, y)
        answer += money[idx][0]
        count += 1
    idx += 1

print(answer)
