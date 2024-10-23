def solution(tickets):
    answer = []
    visit = [0] * len(tickets)
    
    def dfs(airport, path):
        if(len(path) == len(tickets)+1):
            answer.append(path[:])
            return
        
        for idx, ticket in enumerate(tickets):
            if(visit[idx] == 0 and ticket[0] == airport):
                visit[idx] = 1
                path.append(ticket[1])
                dfs(ticket[1], path)
                visit[idx] = 0
                path.pop()
    
    dfs("ICN", ["ICN"])
    
    answer.sort()
    
    return answer[0] 