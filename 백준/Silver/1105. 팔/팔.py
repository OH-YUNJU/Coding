L, R = (input().split())
cnt = 0

if len(L) == len(R):
    for i in range(len(L)):
        if L[i] == '8' and R[i] == '8':
            cnt += 1
        elif L[i] != R[i]:
            break
else:
    cnt = 0

print(cnt)