n, k = map(int, input().strip().split())
a = set(map(int, input().strip().split()))
a = sorted(a)

if k >= len(a):
    print('NO RESULT')
else:
    print(a[k -1])
