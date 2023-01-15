n = int(input())
li = [0, 1]
for i in range(2, abs(n)+1):
    li.append((li[i-1] + li[i-2]) % 1000000000)
if(n % 2 == 0 and n < 0):
    print('-1')
elif(n == 0):
    print('0')
else:
    print(1)
print(li[abs(n)])