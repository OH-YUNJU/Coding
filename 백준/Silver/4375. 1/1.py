while True:
    try:
        n = int(input())
    except:
        exit()
    
    num = 1
    count = 1

    while True:
        if(num % n != 0):
            num = 10 * num + 1
            count += 1
        else:
            break
    print(count)

    