def max_length_in_string(n, s):
    # 알파벳 종류의 최대 개수
    # 투 포인터 사용
    left = 0
    right = 0
    
    # 문자열의 길이
    length = len(s)
    
    # 최대 길이를 기록할 변수
    max_length = 0
    
    # 알파벳 카운트를 기록할 딕셔너리
    char_count = {}
    
    # 현재 윈도우 내에서 종류의 수
    current_distinct_count = 0
    
    # 윈도우를 확장하면서 최대 길이를 계산
    while right < length:
        # 현재 알파벳
        current_char = s[right]
        
        # 알파벳을 딕셔너리에 기록
        if current_char in char_count:
            char_count[current_char] += 1
        else:
            char_count[current_char] = 1
            # 새로운 알파벳 종류가 등장했으므로 카운트 증가
            current_distinct_count += 1
        
        # 종류의 수가 N을 초과할 경우
        while current_distinct_count > n:
            # left 포인터를 이동
            left_char = s[left]
            char_count[left_char] -= 1
            
            # 만약 left_char의 수가 0이면 종류의 수 감소
            if char_count[left_char] == 0:
                del char_count[left_char]
                current_distinct_count -= 1
            
            # left를 한 칸 이동
            left += 1
        
        # 현재 윈도우의 길이
        current_length = right - left + 1
        
        # 최대 길이 갱신
        if current_length > max_length:
            max_length = current_length
        
        # right를 한 칸 이동
        right += 1
    
    return max_length

# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

# 최대 알파벳의 수
n = int(data[0])

# 문자열
s = data[1]

# 최대 길이 계산
result = max_length_in_string(n, s)

# 결과 출력
print(result)
