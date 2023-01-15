n = list(map(int, input().split()))
li = [1,2,3,4,5,6,7,8]

if(n == li):
    print("ascending")
elif(n[::-1] == li):
    print("descending")
else:
    print("mixed")