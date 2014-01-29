i = int(raw_input())
n = map(int, raw_input().split())
cnt=0
 
for i in xrange(len(n)):
    for j in xrange(len(n)-1, i, -1):
        if n[j] < n[j-1]:
            n[j], n[j-1] = n[j-1], n[j]
            cnt+=1
print ' '.join(map(str,n))
print cnt
