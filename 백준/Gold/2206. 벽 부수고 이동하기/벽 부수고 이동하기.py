import sys
from collections import deque

def path_finding():
    visited = [[[0]*2 for _ in range(M)] for _ in range(N)]
    visited[0][0][1] = 1 
    while queue:
        y, x, wall = queue.popleft()
        for dy, dx in move:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < M:
                if maze[ny][nx] == 0 and visited[ny][nx][wall] == 0: 
                    visited[ny][nx][wall] = visited[y][x][wall] + 1
                    queue.append([ny,nx,wall])

                if maze[ny][nx] == 1 and wall == 1: 
                    visited[ny][nx][wall-1] = visited[y][x][wall] + 1 
                    queue.append([ny,nx,wall-1])

    if visited[N-1][M-1][wall] != 0: 
        return visited[N-1][M-1][wall] 
    else: 
        return -1 

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

move = [[1,0], [-1,0], [0,1], [0,-1]]

queue = deque([[0,0,1]])

print(path_finding())