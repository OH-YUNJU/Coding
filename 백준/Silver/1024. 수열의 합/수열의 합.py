N, L = map(int, input().split())
#N = x + x+1 + x+2 + ... + x+L
li = []

for i in range(L, 101):
  x = N - i * (i+1) / 2
  
  if(x % i == 0):
    x = int(x / i)
    
    if(x >= -1):
      for j in range(i):
        li.append(x+1+j)
      break

if(len(li) > 0):
  print(*li)

else:
  print(-1)
