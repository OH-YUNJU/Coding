num = []
for i in range(28):
    num.append(int(input()))

li = [i for i in range(1, 31)]

for i in num:
    li.remove(i)

for i in li:
    print(i)