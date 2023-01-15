import sys
from itertools import combinations
input= sys.stdin.readline
N,M =map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(N)]
#print(maps)
ans=int(1e9)
house=[]
chicken=[]

for i in range(N):
    for j in range(N):
        if maps[i][j]==1:
            house.append((i,j))
        if maps[i][j]==2:
            chicken.append((i,j))

#print(chicken)

for ch in combinations(chicken,M):
    #print(ch)
    citydist=0
    for h in house:
        #각 집마다, 치킨거리
        homeToChicken=2501
        for j in range(M):
            homeToChicken=min(homeToChicken,abs(h[0]-ch[j][0])+abs(h[1]-ch[j][1]))
        #도시의 치킨 거리(치킨 거리의 합)
        citydist+=homeToChicken
    ans=min(ans,citydist)

print(ans)