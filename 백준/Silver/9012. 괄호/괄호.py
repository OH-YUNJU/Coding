def is_vps(ps):
    # 괄호 문자열을 판단할 때 사용하는 변수
    balance = 0
    
    # 문자열의 각 문자에 대해 반복
    for char in ps:
        if char == '(':
            balance += 1  # 여는 괄호면 balance 증가
        elif char == ')':
            balance -= 1  # 닫는 괄호면 balance 감소
        
        # 만약 balance가 음수라면 올바르지 않은 괄호 문자열
        if balance < 0:
            return "NO"
    
    # 모든 문자를 검사하고 balance가 0이라면 올바른 괄호 문자열
    return "YES" if balance == 0 else "NO"

# 입력
import sys
input = sys.stdin.read
data = input().split()

# 테스트 케이스 수
T = int(data[0])

# 각 괄호 문자열을 검사
results = []
for i in range(1, T + 1):
    ps = data[i]
    results.append(is_vps(ps))

# 결과 출력
for result in results:
    print(result)
