n = int(input())
tall = list(map(int, input().split()))
result = [0] * n

for i in range(n):
    cnt = 0
    for j in range(n):
        if(cnt == tall[i] and result[j] == 0):
            result[j] = i+1
            break
        elif(result[j] == 0):
            cnt+=1

print(*result)
