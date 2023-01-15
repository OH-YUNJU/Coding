n = int(input())
queue = []
ans = []

for i in range(n):
    q = list(input().split())
    queue.append(q)

for i in range(n):
    if(queue[i][0] == "push"):
        ans.append(queue[i][1])

    if(queue[i][0] == "pop"):
        if(len(ans) == 0):
            print(-1)
        else:
            print(ans.pop(0))

    if(queue[i][0] == "size"):
        print(len(ans))
    
    if(queue[i][0] == "empty"):
        if(len(ans) == 0):
            print(1)
        else:
            print(0)

    if(queue[i][0] == "front"):
        if(len(ans) == 0):
            print(-1)
        else:
            print(ans[0])

    if(queue[i][0] == "back"):
        if(len(ans) == 0):
            print(-1)
        else:
            print(ans[-1])    
