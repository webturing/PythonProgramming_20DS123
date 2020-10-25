import math
n=int(input().strip())
A=list(map(int,input().strip().split()))
sum=0
min=A[0]
max=A[0]
for x in A:
    sum+=x
    if x>max:max=x
    if x<min:min=x
print(min,max,sum)
