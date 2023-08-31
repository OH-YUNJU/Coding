li = []
for _ in range(9):
  li.append(int(input()))

sumnum = sum(li)

for i in range(8):
  for j in range(i+1, 9):
    if(sumnum - (li[i]) - (li[j])) == 100:
      lie1 = li[i]
      lie2 = li[j]

li.remove(lie1)
li.remove(lie2)

li.sort()
print(*li)