n = int(raw_input())
a = []
for i in ["S","H","C","D"]:
    for j in xrange(1,14):
        a.append("{0} {1}".format(i,j))
for i in xrange(0,n):
    a.remove(raw_input())
for i in a:
    print i
