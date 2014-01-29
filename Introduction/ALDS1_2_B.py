n = int(raw_input())
sec = map(int,raw_input().split())

count = 0
for i in range(0,n):
    mini = i
    for j in range(i,n):
        if sec[j]<sec[mini]:
            mini = j
    if mini != i:
        count += 1
        sec[mini],sec[i] = sec[i],sec[mini]
print " ".join(map(str,sec))
print count
