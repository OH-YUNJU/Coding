n = int(input())
number = []

def dfs():
  if len(number) == n:
    print(*number)
    return
  
  for i in range(1, n+1):
    if i not in number:
      number.append(i)
      dfs()
      number.pop()

dfs()