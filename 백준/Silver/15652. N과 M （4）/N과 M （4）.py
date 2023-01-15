N, M = map(int, input().split())
#visited = [0 for _ in range(N)]
dfs_list = []

def dfs(count):
    if len(dfs_list) == M:
        print(*dfs_list)
        return
    
    for i in range(count, N+1):
        dfs_list.append(i)
        dfs(i)
        dfs_list.pop()
    
dfs(1)