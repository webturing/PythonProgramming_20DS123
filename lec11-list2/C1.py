def bubble_sort(a):
    n = len(a)
    for i in range(n):
        for j in range(n - 2, i - 1, -1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]


a = list(map(int, input().split()))
bubble_sort(a)
for e in a:
    print(e)
