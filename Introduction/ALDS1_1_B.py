l = map(int,raw_input().split())
l.sort()
a,b = l
max = 0
while True:
    tmp = a%b
    if tmp == 0:
        max = b
        break
    a = b
    b = tmp
print max
