n = int(input())
num = list(map(int, input().split()))
ans = int(input())
re = 0

for i in num:
    if(i == ans):
        re+=1
print(re)
