def dfs(numbers, target, length, cal):
    global answer
    
    if(len(numbers) == length and cal == target):
        answer += 1
        return answer
    elif(len(numbers) == length and cal != target):
        return
    
    dfs(numbers, target, length+1, cal+numbers[length])
    dfs(numbers, target, length+1, cal-numbers[length])
    
    return answer

def solution(numbers, target):
    global answer
    answer = 0
    
    dfs(numbers, target, 0, 0)
    
    return answer