while True:
    a,op,b = raw_input().split()
    if op == "?":
        break
    print eval(a+op+b)
