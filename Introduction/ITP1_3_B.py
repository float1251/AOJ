a = []
while True:
    tmp = int(input())
    if tmp == 0:
        break
    else:
        a.append(tmp)
for i,v in enumerate(a):
    print "Case {0}: {1}".format(i+1,v)
