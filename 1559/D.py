import sys

lines = open('D.txt', 'r').readlines()
#lines = sys.stdin.readlines()
for line in lines:
    if not line.strip():
        continue
    a = list(map(int, line.strip().split()))
    del a[0]
    if not a:
        break
    a = sorted(a, key=lambda x: -abs(x))
    for each in a:
        print(each, end=' ')
    print('')
