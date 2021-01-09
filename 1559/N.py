import sys, re

lines = open('N.txt', 'r').readlines()
# lines = sys.stdin.readlines()

del lines[0]
a = [line.strip() for line in lines if line.strip()]
for s in a:
    while len(s) and s == s[::-1] and len(s) % 2 == 0:
        s = s[0:len(s) // 2]
    print(len(s))
