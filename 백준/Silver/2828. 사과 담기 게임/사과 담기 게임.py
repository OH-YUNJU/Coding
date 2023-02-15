n, m = list(map(int, input().split()))
j = int(input())

start = 1
end = m
count = 0

for i in range(j):
    now = int(input())
    if(end >= now and start <= now):
        continue
    elif(start > now):
        count += (start - now)
        end -= (start - now)
        start = now
    else:
        count += (now - end)
        start += (now - end)
        end = now

print(count)