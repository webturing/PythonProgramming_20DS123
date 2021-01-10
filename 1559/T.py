import sys, re, math

lines = open('T.txt', 'r').readlines()


# lines = sys.stdin.readlines()
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


del lines[0]
for line in lines:
    if not line: continue
    a, b, c, d = map(int, line.strip().split())
    up, down = a * d + b * c, b * d
    g = gcd(up, down)
    up //= g
    down //= g
    print(up, down)
