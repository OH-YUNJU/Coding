C = int(input())

for _ in range(C):
    s = input().split()
    
    S = s[0]
    N, T, L = map(int, s[1:])
    
    if S == "O(N)":
        process = N
    elif S == "O(N^2)":
        process = N*N
    elif S == "O(N^3)":
        process = N**3
    elif S == "O(2^N)":
        process = 2**N
    else:
        process = 1
        
        for i in range(2, N+1):
            process *= i
            
            if process > L*10**8:
                break
    
    if T*process <= L*10**8:
        print("May Pass.")
    else:
        print("TLE!")