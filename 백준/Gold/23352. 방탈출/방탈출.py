from collections import deque

class Info:
    def __init__(self, x, y, move):
        self.x = x
        self.y = y
        self.move = move

def bfs(xs, ys):
    global route, ans, start
    q = deque()
    q.append(Info(xs, ys, 0))
    check[xs][ys] = True
    
    while q:
        info = q.popleft()
        x = info.x
        y = info.y
        move = info.move
        end = map[x][y]
        
        if move >= route:
            if move > route:
                ans = start + end
            else:
                ans = max(ans, start + end)
            route = move
        
        for i in range(4):
            x_to = x + x_move[i]
            y_to = y + y_move[i]
            
            if not (0 <= x_to < N and 0 <= y_to < M):
                continue
            if check[x_to][y_to] or map[x_to][y_to] == 0:
                continue
            
            check[x_to][y_to] = True
            q.append(Info(x_to, y_to, move + 1))

# 입력받기
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
map = []
check = [[False] * M for _ in range(N)]

index = 2
for i in range(N):
    map.append([int(data[j]) for j in range(index, index + M)])
    index += M

# 이동 방향 설정 (상, 하, 좌, 우)
x_move = [-1, 1, 0, 0]
y_move = [0, 0, -1, 1]

ans = 0
route = 0

# 모든 방을 탐색하면서 BFS 수행
for i in range(N):
    for j in range(M):
        if map[i][j] != 0:
            check = [[False] * M for _ in range(N)]
            check[i][j] = True
            start = map[i][j]
            bfs(i, j)

# 결과 출력
print(ans)
