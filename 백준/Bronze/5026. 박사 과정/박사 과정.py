n = int(input())
for i in range(n):
    q = input()
    if(q == "P=NP"):
        print("skipped")
        continue
    l, m = map(int, q.split("+"))
    print(l+m)