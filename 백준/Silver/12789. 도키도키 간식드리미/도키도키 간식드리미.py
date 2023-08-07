N = int(input())
first_list = list(map(int, input().split()))
waiting = []
food = 1

while(len(first_list) > 0):
  if(first_list[0] == food):
    first_list.pop(0)
    food += 1
  else:
    waiting.append(first_list[0])
    first_list.pop(0)
 
  while(len(waiting) > 0):
    if(waiting[-1] == food):
      waiting.pop()
      food += 1
    else:
      break

if(len(waiting) == 0):
  print("Nice")
else:
  print("Sad")
                    