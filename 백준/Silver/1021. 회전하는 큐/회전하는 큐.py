from collections import deque

N, M = map(int, input().split())

li = list(map(int, input().split()))

queue = deque(range(1, N+1))

num = 0

for n in li:
    while queue[0] != n:
        tmp = queue.index(n)

        if tmp <= len(queue) - tmp - 1:
            queue.append(queue.popleft())
        else:
            queue.appendleft(queue.pop())
        num += 1
    queue.popleft()

print(num)