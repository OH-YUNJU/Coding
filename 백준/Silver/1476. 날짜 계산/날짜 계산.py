a, b, c = list(map(int, input().split()))
year = 1

while(1):
    if((year-a) % 15 == 0 and (year-b) % 28 == 0 and (year-c) % 19 == 0):
        break
    else:
        year += 1

print(year)