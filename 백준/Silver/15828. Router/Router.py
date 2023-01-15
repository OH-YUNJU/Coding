import sys
input = sys.stdin.readline
n = int(input())
q = []

while 1:
    i = int(input())
    if(i == -1):
        if(len(q) == 0):
            print("empty")
            break
        else:
            print(' '.join(map(str, q)))
        break

    if(i > 0):
        if(len(q) < n):
            q.append(i)
    elif(i == 0):
        q.pop(0)

