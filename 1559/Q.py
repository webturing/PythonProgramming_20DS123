import sys, re

lines = open('Q.txt', 'r').readlines()
# lines = sys.stdin.readlines()

N, T = map(int, lines[0].strip().split())
trees = [1] * (N + 1)
del lines[0]
for line in lines:
    left, right = map(int, line.strip().split())
    trees[left:right + 1] = [0] * (right - left + 1)
print(sum(trees))
