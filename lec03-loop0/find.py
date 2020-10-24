# coding=utf-8
n=int(input())
x=999
flag=False
while x>=100:
    if n%x==0:
        print(x)
        flag=True
        break
    x-=1
if not flag:
    print("NOT FOUND")
