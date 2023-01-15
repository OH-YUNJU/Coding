w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())
 
px = p + t
qx = q + t 
px %= w * 2
qx %= h * 2

if(px > w):
    px = w * 2 - px
if(qx > h):
    qx = h * 2 - qx

print(px)
print(qx)
