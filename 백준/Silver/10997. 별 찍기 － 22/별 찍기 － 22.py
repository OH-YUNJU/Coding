def print_stars(n):
    width = 1 + (n-1) * 4
    height = 1
    
    for i in range(n-1):
        if i == 0:
            height += 6
        else:
            height += 4
    
    # 2차원 배열을 공백으로 초기화
    a = [[' ' for _ in range(width)] for _ in range(height)]
    
    left = 0
    right = width
    top = 0
    bottom = height
    
    for i in range(height):
        for j in range(width):
            if i % 2 == 0:
                if left <= j < right:
                    a[i][j] = '*'
        
        if i < height // 2:
            left += 1
            if i > 1:
                right -= 1
        else:
            if i == height // 2:
                right = height // 2 - 1
            left -= 1
            right += 1
    
    top = 0
    bottom = height
    
    for i in range(width):
        for j in range(height):
            if i % 2 == 0:
                if top <= j < bottom:
                    a[j][i] = '*'
                if i == width - 1 and j == 1:
                    a[j][i] = ' '
        
        if i < width // 2:
            top += 1
            bottom -= 1
        else:
            if i == width // 2:
                top = width // 2 + 2
            top -= 1
            bottom += 1
    
    result = []
    for i in range(height):
        if i == 1:
            result.append(a[i][0])
        else:
            result.append(''.join(a[i]))
        result.append('\n')
    
    print(''.join(result))

# 입력 받기
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    n = int(input().strip())
    print_stars(n)
