n = int(input())
li = list(map(int, input().split()))

li.sort()
left = 0
right = n-1

ans = abs(li[left] + li[right])
now = [li[left], li[right]]

while(left < right):
    left_li = li[left]
    right_li = li[right]

    sum = left_li + right_li

    if(abs(sum) < ans):
        ans = abs(sum)
        now = [left_li, right_li]
        if(ans == 0):
            break
    
    if(sum > 0):
        right -= 1
    else:
        left += 1

print(now[0], now[1])