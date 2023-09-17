from collections import deque

n, m = map(int, input().split())

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, 1, -1 , 1, 1, -1, -1]

result = 0
q = deque()

shark = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
  for j in range(m):
    if(shark[i][j] == 1):
      q.append([i, j])

while q:
  x, y = q.popleft()
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    
    if 0 <= nx < n and 0 <= ny < m:
      if shark[nx][ny] == 0:
        q.append([nx, ny])
        shark[nx][ny] = shark[x][y] + 1
        
for i in range(n):
  for j in range(m):
    result = max(result, shark[i][j])

print(result-1)