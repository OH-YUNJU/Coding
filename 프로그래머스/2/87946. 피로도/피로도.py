from itertools import permutations

def solution(k, dungeons):
    answer = 0
    
    for i in permutations(dungeons, len(dungeons)):
        tmp = k
        cnt = 0
        for less, reduce in i:
            if(tmp >= less):
                tmp -= reduce
                cnt += 1
        
        answer = max(answer, cnt)
    return answer