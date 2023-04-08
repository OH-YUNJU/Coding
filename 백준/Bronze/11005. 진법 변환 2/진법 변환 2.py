N, B = map(int, input().split())
li = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ans = ""
div = N

while(div > 0):
    tmp = int(div % B)
    div = div // B
    ans += str(li[tmp])

print(ans[::-1])