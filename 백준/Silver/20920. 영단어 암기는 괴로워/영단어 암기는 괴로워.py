from operator import itemgetter

n, m = map(int, input().split())
dic = {}

for i in range(n):
  word = input()
  if(len(word) >= m):
    if word in dic:
      dic[word] += 1
    else:
      dic[word] = 1

wordlist = sorted(dic.items(), key = lambda x : (-x[1], -len(x[0]), x[0]))

for i in wordlist:
  print(i[0])