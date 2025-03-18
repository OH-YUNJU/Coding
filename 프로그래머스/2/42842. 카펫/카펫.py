def solution(brown, yellow):
    answer = []
    
    for i in range(1, yellow+1):
        if(yellow % i == 0):
            if(((yellow/i)+2) * (i+2) == yellow+brown):
                answer.append(((yellow/i)+2))
                answer.append((i+2))
                break
    
    if(answer[0] < answer[1]):
        tmp = answer[0]
        answer[0] = answer[1]
        answer[1] = tmp

    return answer