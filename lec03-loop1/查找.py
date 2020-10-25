#找出n的最大三位数因子，如果找不到输出NOT FOUND
n=1007
flag=False
for i in range(999,100-1,-1):
    if n%i==0:
        print(i,end=" ")
        flag=True
        break
if not flag:
    print("NOT FOUND")
