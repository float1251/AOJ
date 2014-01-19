a = [] 
for i in xrange(0,4):
    b = []
    for j in xrange(0,3):
        b.append([0]*10)
    a.append(b)
n = int(raw_input())
for i in xrange(0,n):
    b,f,r,v = map(int,raw_input().split())
    a[b-1][f-1][r-1] += v
for i,arr in enumerate(a):
    for j in arr:
        print " "+" ".join(map(str,j))
    if i != len(a)-1:
        print "#"*20
