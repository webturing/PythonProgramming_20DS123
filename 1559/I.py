import sys


def factorial(n):
    if n <= 1:
        return 1
    else:
        return factorial(n - 1) * n


lines = open('I.txt', 'r').readlines()
#lines = sys.stdin.readlines()

for line in lines:
    if not line.strip(): continue
    n = int(line.strip())
    print(factorial(n))
