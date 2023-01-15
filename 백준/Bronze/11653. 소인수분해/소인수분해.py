num = int(input())
list = []
idx = 2

while num != 1:
    if num % idx==0:
        num /= idx
        list.append(idx)
        idx = 2
    else:
        idx += 1
        
for i in list:
    print(i)