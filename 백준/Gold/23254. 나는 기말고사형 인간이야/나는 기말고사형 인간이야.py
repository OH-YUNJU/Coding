import sys, heapq
input = sys.stdin.readline
n, m = map(int, input().split())
subject_score = list(map(int, input().split()))
subject_plus = list(map(int, input().split()))
subject = []
for i in range(m):
    heapq.heappush(subject, [-subject_plus[i], subject_score[i]])
n *= 24
while subject[0][0] != 0 and n > 0:
    x = heapq.heappop(subject)
    p, s = -x[0], x[1]
    quotient = (100 - s) // p  
    if n >= quotient:
        n -= quotient
    else:
        quotient = n
        n = 0
    s = quotient * p + s
    p = 100 - s
    heapq.heappush(subject, [-p, s])
score = 0
for x in subject:
    score += x[1]
print(score)