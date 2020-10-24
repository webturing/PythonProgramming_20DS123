# coding=utf-8
x=1 
s=0 # 1累加器清0
while x<=100: #循环条件
    if x%3==0 or x%5==0:
        s+=1 #3.动作
    x+=1 
print(s)
