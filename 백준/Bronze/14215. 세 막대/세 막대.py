li = sorted(map(int, input().split()))
ans = li[0] + li[1] + min(li[2], li[0]+li[1]-1)
print(ans)