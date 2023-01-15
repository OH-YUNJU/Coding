dx = [-1, 1, 0, 0]	
dy = [0, 0, -1, 1]

def dfs(x, y):
    
    global result
    
    visited[x][y] = 1
    
    for i in range(4):
        X = x + dx[i]
        Y = y + dy[i]
        
        if 0 <= X < N and 0 <= Y < E:	
            if dots[X][Y] == dots[x][y]:		
                if visited[X][Y] == 0:	
                    game.append([X, Y])		
                    dfs(X, Y)	
                    game.pop()
                    
                else:		
                    if X == game[-2][0] and Y == game[-2][1]:
                        pass
                    
                    else:	
                        result = 'Yes'	
                        return
                    
        if result == 'Yes':
            return

N, E = map(int, input().split())

dots = []

visited = [[0] * E for _ in range(N)]

for _ in range(N):
    dots.append(input())

result = 'No'

for i in range(N):
    for j in range(E):
        if visited[i][j] == 0:	
            game = [[i, j]]	
            dfs(i, j)
            
        if result == 'Yes':
            break
        
    if result == 'Yes':
        break

print(result)
