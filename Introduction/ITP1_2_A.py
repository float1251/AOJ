a,b = map(int,raw_input().split())
if a == b:
    str = "{0} == {1}"
elif a < b:
    str = "{0} < {1}"
else:
    str = "{0} > {1}"
print str.format("a","b")


