import sys, re, math

lines = open('U.txt', 'r').readlines()

# lines = sys.stdin.readlines()


for i in range(2, len(lines), 2):
    arr = map(int, lines[i].strip().split())
    print(len(set(arr)))
