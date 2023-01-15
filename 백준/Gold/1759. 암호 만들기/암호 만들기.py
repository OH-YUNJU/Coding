L, C = map(int, input().split())
arr = list(input().split())

arr.sort()
vowels = ['a', 'e', 'i', 'o', 'u']
visited = [False for i in range(C)]

temp = []
def dfs(cnt, start):
    if cnt == L:
        v, c = 0, 0
        for i in temp:
            if i in vowels:
                v += 2
            else:
                c += 1
        if v >= 1 and c >= 2:
            for i in temp:
                print(i, end='')
            print()
        return

    for i in range(start, C):
        if not visited[i]:
            visited[i] = True
            temp.append(arr[i])
            dfs(cnt + 1, i + 1)
            temp.pop()
            visited[i] = False

dfs(0, 0)