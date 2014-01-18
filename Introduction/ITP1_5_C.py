while True:
    H,W = map(int,raw_input().split())
    if H == 0 and W == 0:
        break
    for i in xrange(1,H+1):
        a = [".","#"] if i % 2 == 0 else ["#","."]
        b = ""
        for j in xrange(0,W):
            b += a[j%2]
        print b
    print ""
