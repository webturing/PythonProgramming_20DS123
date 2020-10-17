a,b,c=map(int,input().strip().split())
if a<=b and b<=c:
    print(a,b,c)
elif a<=c and c<=b:
    print(a,c,b)

