def solution(mats, park):
    answer = 0
    park_x = len(park[0])
    park_y = len(park)
    mat_posit = []
    
    sortmat = sorted(mats, reverse=True)
    
    for y in range(park_y):
        for x in range(park_x):
            
            for mat in sortmat:
                mat_TF = False
                if(y+mat > park_y or x+mat > park_x):
                    continue
                    
                for i in range(mat):
                    if mat_TF:
                        break
                    for j in range(mat):
                        if(park[y+i][x+j] != "-1"):
                            mat_TF = True
                            break
                if not mat_TF:
                    mat_posit.append(mat)
                    break
    if mat_posit:
        answer = max(mat_posit)
    else:
        answer = -1
    
    return answer