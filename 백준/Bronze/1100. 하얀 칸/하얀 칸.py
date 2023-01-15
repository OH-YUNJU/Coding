li = []
count = 0

for _ in range(8):
    li.append(input())
for i in range(8):
    for j in range(8):
        if i % 2 == 1 and j % 2 == 1 and li[i][j] == "F":
            count += 1
        if i % 2 == 0 and j % 2 == 0 and li[i][j] == "F":
            count += 1
print(count)