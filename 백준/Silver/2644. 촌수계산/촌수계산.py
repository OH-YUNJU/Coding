n = int(input())
a, b = map(int, input().split())
m = int(input())
graph = [[] for i in range(n+1)]
visit = [False] * (n+1)
result = []

def dfs(v, num):
  num += 1
  visit[v] = True

  if(v == b):
    result.append(num)
  
  for i in graph[v]:
    if not visit[i]:
      dfs(i, num)
  
for _ in range(m):
  x, y = map(int, input().split())
  graph[x].append(y)
  graph[y].append(x)

dfs(a, 0)

if(len(result) == 0):
  print(-1)
else:
  print(result[0]-1)

