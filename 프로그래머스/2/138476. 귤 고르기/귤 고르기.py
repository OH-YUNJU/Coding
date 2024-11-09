def solution(k, tangerine):
    answer = 0
    dict = {}
    
    for i in tangerine:
        if(i not in dict):
            dict[i] = 1
        else:
            dict[i] += 1
    
    sort_dict = sorted(dict.values(), reverse=True)
    
    for count in sort_dict:
        k -= count
        answer += 1
        
        if k <= 0:
            break
    
    return answer