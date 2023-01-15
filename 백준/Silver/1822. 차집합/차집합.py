import sys
a,b=map(int, sys.stdin.readline().split())
set1=set(map(int,sys.stdin.readline().split()))
set2=set(map(int,sys.stdin.readline().split()))
cnt=0
ans=[]
for i in set1:
    if i not in set2:
        cnt+=1
        ans.append(i)
print(cnt)
if cnt!=0 :
    ans.sort()
    print(*ans)
