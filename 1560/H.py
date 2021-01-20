n = int(input())
a = list(map(int, input().strip().split()))
a.sort()
book = [0] * n
s = 0
p = n - 1
q = 0

for i in range(n):
    s += (a[p] - q) ** 2
    book[p] = 1
    q = a[p]
    p = n - 1 - p
    if book[p]:
        if p < n // 2:
            p += 1
        else:
            p -= 1
print(s)
