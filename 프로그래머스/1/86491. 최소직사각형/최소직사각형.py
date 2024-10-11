def solution(sizes):
    answer = 0
    ga = []
    se = []
    
    for a, b in sizes:
        if(a < b):
            ga.append(b)
            se.append(a)
        else:
            ga.append(a)
            se.append(b)
    
    answer = max(ga) * max(se)
            
    return answer