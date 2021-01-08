import sys
lines = sys.stdin.readlines()

for line in lines:
    a = list(map(int, line.strip().split()))
    if a[0] == 0:
        break
    del a[0]
    a = sorted(a, key=lambda x: -abs(x))
    for e in a:
        print(e, end=' ')
    print('')
