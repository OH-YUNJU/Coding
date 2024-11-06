def solution(brown, yellow):
    answer = []
    
    tmp = (brown - 4) / 2
    
    for i in range(1, yellow+1):
        if(i + (yellow/i) == tmp):
            answer.append(i+2)
            answer.append(yellow/i+2)
            break
    
    answer.sort(reverse=True)
    
    return answer