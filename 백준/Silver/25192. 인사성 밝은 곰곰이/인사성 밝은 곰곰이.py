n = int(input())
chat = {}
emo = 0

for i in range(n):
  name = input()
  if name not in chat.keys() and name != "ENTER":
    emo += 1
  chat[name] = 1
  
  if name in chat.keys() and name == "ENTER":
    chat = {}
    chat[name] = 1

print(emo)