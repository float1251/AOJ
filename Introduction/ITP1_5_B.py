while True:
    H,W = map(int,raw_input().split())
    if H == 0 and W == 0:
        break
    a = "#"
    b = "."
    for i in xrange(0,H):
        if i == 0 or i == H-1:
            print a * W
        else: 
            c = W - 2
            print a+b*c+a
    print ""
