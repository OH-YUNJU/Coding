def solution(numbers):
    answer = ''
    
    for i in range(len(numbers)):
        numbers[i] = str(numbers[i])
    numbers.sort(key = lambda x: x*3, reverse=True)
    
    for i in range(len(numbers)):
        answer = answer+numbers[i]
    
    answer = int(answer)
    answer = str(answer)
    
    return answer