import sys, re

lines = open('O.txt', 'r').readlines()
# lines = sys.stdin.readlines()

a = list(map(int, lines[1].strip().split()))
a = sorted(set(a))
print(len(a))
for each in a:
    print(each, end=' ')
print()
