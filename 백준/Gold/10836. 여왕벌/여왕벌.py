import sys 
input = sys.stdin.readline

M, N = map(int, input().split())
larva = [1 for _ in range(2*M+1)]

for _ in range(N):
    zero, one, two = map(int, input().split())
        
    for i in range(zero, zero + one): 
            larva[i] += 1
        
    for i in range(zero+one, zero+one+two):
            larva[i] += 2

for i in range(M):
    for j in range(M):
        if j == 0:
            print(larva[M - (i + 1)])
        else:
            print(larva[M + j - 1])