while 1:
    li = sorted(map(int, input().split()))
    if (li[0] == li[1] == li[2] == 0):
        break
    if (li[2] >= li[0] + li[1]):
        print("Invalid")

    elif (li[0] == li[1] == li[2]):
        print("Equilateral")
    elif (li[0] == li[1] or li[1] == li[2] or li[0] == li[2]):
        print("Isosceles")
    elif (li[0] != li[1] != li[2]):
        print("Scalene")