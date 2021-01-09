import sys, re

lines = open('M.txt', 'r').readlines()
#lines = sys.stdin.readlines()

del lines[0]
numbers = [int(line.strip()) for line in lines if line.strip()]
for n in numbers:
    print(n * (n + 1) * (n + 2) // 6)
