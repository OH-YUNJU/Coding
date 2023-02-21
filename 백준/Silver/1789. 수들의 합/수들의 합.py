import math

num = int(input())
m = int(math.sqrt(2*num))

while(m * m + m > 2*num):
    m-= 1

print(m)