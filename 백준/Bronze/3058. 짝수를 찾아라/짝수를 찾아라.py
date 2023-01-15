T = int(input())

for i in range(T):
    li = []
    num = list(map(int, input().split()))
    for i in num:
        if i % 2 == 0:
            li.append(i)
    print(sum(li), min(li))