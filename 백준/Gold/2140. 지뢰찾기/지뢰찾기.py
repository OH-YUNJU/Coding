N = int(input())
board = [list(input()) for _ in range(N)]

for r in range(N):
    for c in range(N):
        if board[r][c] in ('#', 'O', 'X'):
            continue
        target = int(board[r][c])
        checked = 0
        bombs = 0
        for ir in (-1,0,1):
            for ic in (-1,0,1):
                checked += 1
                if ir==0 and ic==0: continue
                nr, nc = r+ir, c+ic
                if 0 <= nr < N and 0 <= nc < N:
                    if board[nr][nc] == '#':
                        if bombs == target:
                            board[nr][nc] = 'X'
                        else:
                            board[nr][nc] = 'O'
                            bombs += 1
                    elif board[nr][nc] == 'O':
                        bombs += 1

print(sum(int(board[r][c] in ('#', 'O')) for r in range(N) for c in range(N)))