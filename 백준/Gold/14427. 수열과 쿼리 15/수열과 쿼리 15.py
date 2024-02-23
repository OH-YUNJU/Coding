#세그먼트 트리
#O(logN)
#메모리 시간복잡도 

import sys
input=sys.stdin.readline

n = int(input())
quary = list(map(int,input().split()))
arrindex = []
for i in range(n):
    arrindex.append([quary[i], i+1])

tree=[0]*(n*4)

def init(start, end, index):
    if(start == end):
        tree[index] = arrindex[start]
    else:
        mid = (start+end) // 2
        tree[index] = min(init(start, mid, index*2), init(mid+1, end, index*2+1))
    
    return tree[index]

def update(start, end, index, a, v):
    if(a < start or a > end):
        return 

    if(start == end):
        tree[index] = v
        return tree[index]

    mid=(start + end) // 2
    update(start, mid, index*2, a, v)
    update(mid+1, end, index*2+1, a, v)

    tree[index] = min(tree[index*2], tree[index*2+1])
    
def do_one(start, end, index, left, right):
    if(start > right or end < left):
        return [sys.maxsize, sys.maxsize]

    if(start >= left and end <= right):
        return tree[index]

    mid = (start+end) // 2
    return min(do_one(start, mid, index*2, left, right), do_one(mid+1, end, index*2+1, left, right))
 
init(0,n-1,1)

for j in range(int(input())):
    quary = list(map(int,input().split())) 

    if quary[0] == 1:
        arrindex[quary[1]-1][0] = quary[2]
        update(0, n-1, 1, quary[1]-1, arrindex[quary[1]-1])
     
    elif quary[0] == 2:
        print(do_one(0, n-1, 1, 0, n-1)[1])
