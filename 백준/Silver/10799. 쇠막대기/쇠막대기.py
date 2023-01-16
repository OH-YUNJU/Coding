stick = list(input())
stack = []
result = 0

for i in range(len(stick)):
    if(stick[i] == "("):
        stack.append(stick[i])
    if(stick[i] == ")"):
        if(stick[i-1] == ")"):
            stack.pop()
            result += 1
        else:
            stack.pop()
            result += len(stack)

print(result)