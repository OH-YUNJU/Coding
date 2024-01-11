from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0] * bridge_length
    bridge = deque(bridge)
    truck_weights = deque(truck_weights)
    sumbridge = 0
    
    while truck_weights:
        answer += 1
        sumbridge -= bridge.popleft()
        
        if(sumbridge + truck_weights[0] <= weight):
            sumbridge += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
            
    answer += bridge_length
        
    return answer