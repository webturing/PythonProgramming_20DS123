# coding=utf-8
n = int(input())
a = []
for i in range(n):
    k = sum(map(int, input().strip().split()))
    if k not in a:
        a.append(k)
t = a[0]
a.sort()
a.reverse()
if t >= a[2]:
    print('yes')
else:
    print('no')
print(a.index(t) + 1)
