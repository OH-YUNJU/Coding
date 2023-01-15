import sys
 
 
N = int(sys.stdin.readline())
ring_list=list(map(int,sys.stdin.readline().split()))

def gcd(a,b):
    if a > b:
        a, b = b, a
 
    g = b
    r = a % b
    while r != 0: 
        tmp = r
        r = g % r
        g = tmp
 
    return g
 
for i in range(1,len(ring_list)):
    g=gcd(ring_list[0],ring_list[i])
    print(ring_list[0]//g,end="/")
    print(ring_list[i]//g)