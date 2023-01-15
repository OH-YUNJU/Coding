origin = [1,1,2,2,2,8]
cur = list(map(int,input().split()))
for i in range(6):
    print(origin[i]-cur[i],end=" ")