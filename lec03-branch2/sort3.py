while True:
    a,b,c=map(int,input().strip().split())
    small = a
    if b < small:
        small = b
    if c < small:
        small = c
    big = a
    if b > big:
        big = b
    if c > big:
        big = c
    mid = a + b + c - small - big
    print(small,mid,big)
