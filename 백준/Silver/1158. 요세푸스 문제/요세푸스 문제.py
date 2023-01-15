from collections import deque

n, k = list(map(int, input().split()))
q = deque()
ans = []

for i in range(1, n+1):
    q.append(i)

for _ in range(n):
    for _ in range(k-1):
        q.append(q.popleft())
    ans.append(q.popleft())

print(str(ans).replace('[', '<').replace(']', '>'))


