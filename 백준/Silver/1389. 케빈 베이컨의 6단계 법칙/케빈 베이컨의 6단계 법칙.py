from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
result = []

def bfs(graph, first):
  visit = [first]
  bacon = [0] * (n+1)
  queue = deque()
  queue.append(first)
  
  while queue:
    a = queue.popleft()
    for i in graph[a]:
      if i not in visit:
        bacon[i] = bacon[a] + 1
        visit.append(i)
        queue.append(i)
  return sum(bacon)
  

for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  graph[b].append(a)

for i in range(1, n+1):
  result.append(bfs(graph, i))

print(result.index(min(result)) + 1)