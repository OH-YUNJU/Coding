from collections import deque

def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    
    while queue:
        maxnum = max(queue)
        num = queue.popleft()
        location -= 1
        
        if(num < maxnum):
            queue.append(num)
            
            if(location < 0):
                location = len(queue) - 1
        else:
            answer += 1
        
        if(location < 0):
            return answer
