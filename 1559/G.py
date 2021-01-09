import sys

# lines = open('G.txt', 'r').readlines()
lines = sys.stdin.readlines()
for line in lines:
    if not line.strip(): continue
    for char in line.strip():
        if char == '1':
            print(0, end='')
        else:
            print(1, end='')
    print('')
