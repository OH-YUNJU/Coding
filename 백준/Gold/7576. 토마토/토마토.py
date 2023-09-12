from collections import deque

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

queue = deque()
result = 0

for i in range(n):
  for j in range(m):
    if(tomato[i][j] == 1):
      queue.append([i, j])
        
def bfs():
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx, ny = dx[i] + x, dy[i] + y
      if(0 <= nx < n and 0 <= ny < m and tomato[nx][ny] == 0):
        tomato[nx][ny] = tomato[x][y] + 1
        queue.append([nx, ny])
bfs()

for i in range(n):
  for j in range(m):
    if(tomato[i][j] == 0):
      print(-1)
      exit()
    result = max(result, tomato[i][j])
print(result-1)