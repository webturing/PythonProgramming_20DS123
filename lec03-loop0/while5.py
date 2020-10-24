# coding=utf-8
x=0
while x<3*5*7:
    if x%3==1 and x%5==2 and x%7==3:
        print(x)
        break
    x+=1
