from collections import deque

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
queue = deque()
maxnum = 0
cnt = 0
result = 0

for i in range(n):
  for j in range(n):
    if(area[i][j] > maxnum):
      maxnum = area[i][j]
    
def bfs(x, y, visited, maxnum):
  queue.append([x, y])
  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if(0 <= nx < n and 0 <= ny < n):
        if(visited[nx][ny] == 0 and area[nx][ny] > maxnum):
          visited[nx][ny] = 1
          queue.append([nx, ny])

for i in range(maxnum):
  visited = [[0] * n for _ in range(n)]
  cnt = 0
  for j in range(n):
    for k in range(n):
      if(area[j][k] > i and visited[j][k] == 0):
        bfs(j, k, visited, i)
        cnt += 1
  if result < cnt:
    result = cnt

print(result)
    