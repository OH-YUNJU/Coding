def solution(s):
    answer = True
    
    num = 0

    for i in s:
        if(i == '('):
            num += 1
        elif(i == ')'):
            num -= 1
        if(num < 0):
            answer = False

    if(num != 0):
        answer = False

    return answer