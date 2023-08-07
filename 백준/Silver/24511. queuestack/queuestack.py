import sys
from collections import deque

N = int(sys.stdin.readline())
queue_or_stack = list(map(int, sys.stdin.readline().split())) #큐인지 스택인지
queuestack = list(map(int, sys.stdin.readline().split())) #기존 자료구조

newnum = int(sys.stdin.readline()) #새로넣을 수열 길이
newli = list(map(int, sys.stdin.readline().split())) #새로넣을 수열

queue = deque([]) #합칠 하나의 큐

for i in range(N):
  if(queue_or_stack[i] == 0):
    queue.appendleft(queuestack[i])
    
if(len(queue) <= 0):
  print(*newli)
  sys.exit()

for i in range(newnum):
  queue.append(newli[i])
  print(queue.popleft(), end=" ")
    