import sys, re

lines = open('P.txt', 'r').readlines()
# lines = sys.stdin.readlines()

a = list(map(int, lines[1].strip().split()))
Q = []
for x in a:
    Q.append(x)
while Q:
    print(Q[0], end=' ')
    del Q[0]
    if Q:
        x = Q[0]
        del Q[0]
        Q.append(x)
