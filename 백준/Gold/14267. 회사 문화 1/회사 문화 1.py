import sys

sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
immediate_superior_list = list(map(int, input().split()))

immediate_subordinate = [[] for _ in range(n + 1)]  
immediate_superior = [0] * (n + 1)
for i in range(1, len(immediate_superior_list)):
    immediate_subordinate[immediate_superior_list[i]].append(i + 1)
    immediate_superior[i + 1] = immediate_superior_list[i]

compliment = [0] * (n + 1)


def pre_order(n): 
    compliment[n] += compliment[immediate_superior[n]]  
    if immediate_subordinate[n]: 
        for i in range(len(immediate_subordinate[n])): 
            pre_order(immediate_subordinate[n][i])


for i in range(m):  
    receiver, com_value = map(int, input().split())  
    compliment[receiver] += com_value 

pre_order(1)

compliment.pop(0) 
print(*compliment)