a, b = map(int, input().split())
alist = set(map(int, input().split()))
blist = set(map(int, input().split()))

aans = alist - blist
bans = blist - alist
print(len(aans) + len(bans))
