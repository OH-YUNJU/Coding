li = [ list(map(int, input().split())) for i in range(9) ]
max = 0
a,b = 0,0

for i in range(9):
    for j in range(9):
        if(max < li[i][j]):
            max = li[i][j]
        if(max == li[i][j]):
            a = i+1
            b = j+1

if(a == 0 and b == 0):
    print(max)
else:
    print(max)
    print(a, b)
