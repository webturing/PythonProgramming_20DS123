import sys, re, math

# line = open('V.txt', 'r').readline()

line = sys.stdin.readline()

n = int(line.strip())
if n % 2 == 0:
    n //= 2
    for i in range(10 ** (n - 1), 10 ** n):
        s = str(i)
        print(s + s[::-1])
else:
    n = n // 2 + 1
    for i in range(10 ** (n - 1), 10 ** n):
        s = str(i)
        print(s + s[::-1][1:])
