n, k = map(int, input().split())
li = []
for _ in range(n):
    nara = list(map(int, input().split()))
    if(nara[0] != k):
        li.append(nara)
    else:
        ranking = nara
rank = 1

for i in range(len(li)):
    if(li[i][1] > ranking[1]):
        rank += 1
    elif(li[i][1] == ranking[1]):
        if(li[i][2] > ranking[2]):
            rank += 1
        elif(li[i][2] == ranking[2]):
            if(li[i][3] > ranking[3]):
                rank += 1

print(rank)

