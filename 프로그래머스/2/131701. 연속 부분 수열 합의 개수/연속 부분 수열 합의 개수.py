from collections import deque

def solution(elements):
    answer = set()
    
    deq = deque(elements)
    
    for i in range(len(elements)):
        sum = 0
        for e in deq:
            sum += e
            answer.add(sum)
        
        deq.append(deq.popleft())
    
    return len(answer)