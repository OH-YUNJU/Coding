S = list(input())
K = input()
li = []
for i in S:
    if ord(i) <= 122 and ord(i) >= 97 or ord(i) <= 90 and ord(i) >= 65:
        li.append(i)
li = ''.join(li)

if K in li:
    print(1)
else:
    print(0)