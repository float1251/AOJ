a,b = map(int,raw_input().split())
d = int(a/b)
r = a % b
f = a / float(b)
print d,r,"{0:.5f}".format(f)
