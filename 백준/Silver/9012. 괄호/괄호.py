def is_vps(ps):
    balance = 0
    
    for char in ps:
        if char == '(':
            balance += 1 
        elif char == ')':
            balance -= 1 
        
        if balance < 0:
            return "NO"
    
    return "YES" if balance == 0 else "NO"

import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])

results = []
for i in range(1, T + 1):
    ps = data[i]
    results.append(is_vps(ps))

for result in results:
    print(result)
