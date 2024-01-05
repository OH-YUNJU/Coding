import math

def solution(progresses, speeds):
    answer = []
    bepo = 1

    for i in range(len(progresses)):
        progresses[i] = math.ceil((100 - progresses[i]) / speeds[i])
    #print(progresses)
    
    bepolist = progresses[0]
    
    for j in range(1, len(progresses)):
        if(bepolist < progresses[j]):
            answer.append(bepo)
            bepolist = progresses[j]
            bepo = 1
        else:
            bepo += 1
            
    answer.append(bepo)
    
    return answer