n = int(input())
li = []
for i in range(n):
    rope = int(input())
    li.append(rope)

li.sort(reverse=True)

for i in range(1, n+1):
    li[i-1] = li[i-1]*i

print(max(li))
