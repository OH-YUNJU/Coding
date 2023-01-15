n, k = map(int, input().split())
nn = list(map(int, input().split())) # 리스트로 int를 바로 입력받기

nn.sort(reverse=True) # 큰 수부터 정렬 (역정렬)
print(nn[k-1])
