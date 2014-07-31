try:
    while True:
        n = int(input())
        count = 0
        for a in range(10):
            for b in range(10):
                for c in range(10):
                    for d in range(10):
                        if a+b+c+d == n:
                            count += 1
        print(count)
except:
    pass
