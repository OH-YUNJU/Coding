def solution(n, lost, reserve):
    answer = 0
    
    cloth = [1] * n
    
    for l in lost:
        cloth[l-1] -= 1
    for r in reserve:
        cloth[r-1] += 1
    
    for i in range(n):
        if(cloth[i] == 0):
            if((0 <= i-1 < n) and cloth[i-1] > 1):
                cloth[i] += 1
                cloth[i-1] -= 1
            elif((0 <= i+1 < n) and cloth[i+1] > 1):
                cloth[i] += 1
                cloth[i+1] -= 1
        
    for k in range(n):
        if(cloth[k] > 0):
            answer += 1
               
    return answer