import sys

n1 = int(sys.stdin.readline())
li1 = []
for i in range(n1):
    li1.append(int(sys.stdin.readline()))
n2 = int(sys.stdin.readline())
li2 = []
for j in range(n2):
    li2.append(int(sys.stdin.readline()))
n3 = int(sys.stdin.readline())
li3 = []
for k in range(n3):
    li3.append(int(sys.stdin.readline()))

def cal(a):
    if(a > 0):
        print("+")
    elif(a == 0):
        print("0")
    else:
        print("-")

cal(sum(li1))
cal(sum(li2))
cal(sum(li3))