import sys, re, math

lines = open('S.txt', 'r').readlines()

# lines = sys.stdin.readlines()

for line in lines:
    if not line: continue
    a, b = map(lambda x: int(x, 16), line.strip().split())
    print(a + b)
