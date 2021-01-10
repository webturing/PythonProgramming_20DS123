import sys, re, math

lines = open('R.txt', 'r').readlines()


# lines = sys.stdin.readlines()

def prime(n):
    if n == 2: return True
    if n < 2 or n % 2 == 0: return False
    for c in range(3, int(math.sqrt(n)) + 1, 2):
        if n % c == 0: return False
    return True


def check(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return prime(n // i)
    return False


N = int(lines[0].strip())
del lines[0]
for line in lines:
    n = int(line.strip())
    if check(n):
        print('Yes')
    else:
        print('No')
