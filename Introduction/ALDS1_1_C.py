def main():
    N = int(raw_input())
    s = [int(raw_input()) for x in range(N)]
    count = 0
    for i in s:
        if is_prime(i):
            count +=1
    print count
    
def is_prime(q):
    q = abs(q)
    if q == 2: return True
    if q < 2 or q&1 == 0: return False
    return pow(2, q-1, q) == 1

main()
