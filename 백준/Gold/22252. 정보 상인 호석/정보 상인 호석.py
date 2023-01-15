import sys, heapq
input = sys.stdin.readline
Q = int(input())
gorilla = {}
name = set()
result = 0
for _ in range(Q):
    q = input().split()
    if q[0] == '1':
        if q[1] not in name:
            gorilla[q[1]] = []
            name.add(q[1])
        for x in q[3:]:
            heapq.heappush(gorilla[q[1]], -int(x))
    else:
        if q[1] not in name:
            continue
        for _ in range(min(int(q[2]), len(gorilla[q[1]]))):
            result += -heapq.heappop(gorilla[q[1]])
print(result)
