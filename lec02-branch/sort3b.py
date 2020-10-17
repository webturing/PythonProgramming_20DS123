<<<<<<< HEAD
a,b,c=map(int,input().strip().split())
if a<=b and b<=c:
    print(a,b,c)
elif a<=c and c<=b:
    print(a,c,b)

=======
a, b, c = map(int, input().strip().split())
if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a
print(a, b, c)
>>>>>>> 477c5456a21cf437c334c85c8db56f65a467d75f
