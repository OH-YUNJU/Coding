n, k = map(int, input().split())
score = []
for i in range(n):
    score.append(float(input()))
score = sorted(score)
jul, bo = 0, 0

jul = sum(score[k:n-k]) / (n-k-k)
bo = (sum(score[k:n-k])+score[k]*k+score[n-k-1]*k) / n

print("{:.2f}".format(jul+1e-8))
print("{:.2f}".format(bo+1e-8))