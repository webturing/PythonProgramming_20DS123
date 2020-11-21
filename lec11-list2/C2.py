def select_sort(a):
    n = len(a)
    for i in range(n):
        k = i
        for j in range(i + 1, n):
            if a[j] < a[k]:
                k = j
        if k != i:
            a[i], a[k] = a[k], a[i]


a = list(map(int, input().split()))
select_sort(a)
for e in a:
    print(e)
