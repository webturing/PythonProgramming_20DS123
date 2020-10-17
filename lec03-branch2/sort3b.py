while True:
    a,b,c=map(int,input().strip().split())
    if a > b:
        t = a
        a = b
        b = t
    if b>c:
        b,c=c,b
    if a>c:
        a,c=c,a
    print(a,b,c)
        
