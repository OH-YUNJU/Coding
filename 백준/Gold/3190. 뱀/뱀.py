from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def simulate(n, k, apples, l, turns):
    board = [[0] * (n + 1) for _ in range(n + 1)] 
    for x, y in apples:
        board[x][y] = 1  
    direction = 0 
    snake = deque([(1, 1)])  
    time = 0  
    idx = 0 

    while True:
        time += 1
        nx, ny = snake[-1][0] + dx[direction], snake[-1][1] + dy[direction] 
        if 1 <= nx <= n and 1 <= ny <= n and (nx, ny) not in snake: 
            snake.append((nx, ny))  
            if board[nx][ny] == 0:  
                snake.popleft()  
            else:  
                board[nx][ny] = 0 
            
            if idx < l and time == int(turns[idx][0]):  
                if turns[idx][1] == 'D': 
                    direction = (direction + 1) % 4
                else: 
                    direction = (direction - 1) % 4
                idx += 1
        else:  
            break

    return time

n = int(input())  
k = int(input())  #
apples = [tuple(map(int, input().split())) for _ in range(k)]  
l = int(input())  
turns = [input().split() for _ in range(l)]  

print(simulate(n, k, apples, l, turns))
