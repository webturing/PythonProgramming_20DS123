def insert_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(i - 1, 0 - 1, -1):
            if a[j] < a[j + 1]:
                break
            a[j], a[j + 1] = a[j + 1], a[j]


a = list(map(int, input().split()))
insert_sort(a)
for e in a:
    print(e)
