#统计1-n中的偶数个数
cnt=0
for i in range(1,n+1):
    if i%2==0:
        cnt+=1
print(cnt)
