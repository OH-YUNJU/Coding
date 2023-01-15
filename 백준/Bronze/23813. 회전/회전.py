num = str(input())

def p(num):
    ans=0
    for i in range(len(num)):
        ans += int(num[1:] + num[0])
        num = num[1:] + num[0]
    print(ans)

p(num)
