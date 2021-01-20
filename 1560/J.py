while True:
    a = sorted(map(int, input().strip().split()))
    print((a[2] * 100 + a[1] * 10 + a[0]) * a[3])
