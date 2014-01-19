while True:
    n,x = map(int,raw_input().split())
    if n == 0 and x == 0:
        break
    count = 0
    for a in xrange(1,n+1):
        for b in xrange(1,n+1):
            if a == b:
                break
            for c in xrange(1,n+1):
                if a == c or b == c:
                    break
                if a+b+c == x:
                    count +=1
    print count
