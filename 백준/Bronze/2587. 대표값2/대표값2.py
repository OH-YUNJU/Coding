li = []
ans = 0
for i in range(5):
    li.append(int(input()))

li.sort()
for i in li:
    ans += i

print(int(ans/5))
print(li[2])