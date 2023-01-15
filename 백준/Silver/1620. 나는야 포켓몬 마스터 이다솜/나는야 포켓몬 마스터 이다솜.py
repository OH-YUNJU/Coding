n, m = list(map(int, input().split()))
li = {}
num = []

for i in range(n):
    pokemon = input()
    li[pokemon] = i+1
    num.append(pokemon)
for i in range(m):
    name = input()
    if(name in li):
        print(li[name])
    else:
        print(num[int(name)-1])