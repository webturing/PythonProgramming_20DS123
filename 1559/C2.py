
if __name__ == '__main__':
    n = 9
    n = int(input().strip())
    a = list(range(1, n+1))
    for i in range(2, n):
        a[i] *= a[i-1]
    print(sum(a))
