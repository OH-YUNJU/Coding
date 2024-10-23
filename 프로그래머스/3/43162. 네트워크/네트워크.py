def solution(n, computers):
    answer = 0
    visit = [0] * n
    
    def dfs(i):
        for j in range(n):
            visit[i] = 1
            if(visit[j] == 0 and computers[i][j] == 1):
                dfs(j)
        
        
    for i in range(n):
        if(visit[i] == 0):
            dfs(i)
            answer += 1
    
    return answer