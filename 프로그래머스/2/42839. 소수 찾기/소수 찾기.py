from itertools import permutations

def solution(numbers):
    answer = set()
    
    def prime(n):
        if n < 2:  
            return -1
        
        for i in range(2, n):
            if(n % i == 0):
                return -1
        return n
            
    for length in range(1, len(numbers)+1):
        for number in permutations(numbers, length):
            number = int(''.join(number))
            
            if(prime(number) == number):
                answer.add(number)
            
    answer = len(answer)
    
    return answer