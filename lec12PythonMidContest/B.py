import math
while True:
    a, b = map(int, input().split())
    if a!=b:
        print(max(a,b))
    else:
        print(a,b)
