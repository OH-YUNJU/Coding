def solution(data, ext, val_ext, sort_by):
    answer = []
    dict = {
        "code" : 0,
        "date" : 1,
        "maximum" : 2,
        "remain" : 3
    }
    for i in data:
        pos = i[dict[ext]]
        
        if(pos < val_ext):
            answer.append(i)
            
    answer.sort(key=lambda a:a[dict[sort_by]])
    
    return answer