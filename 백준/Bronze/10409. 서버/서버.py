n, T = map(int, input().split())
task = map(int, input().split())
answer = 0

for i in task:
    T -= i
    if T < 0:
        break
    answer += 1

print(answer)