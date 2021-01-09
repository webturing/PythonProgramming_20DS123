import sys, re

# line = open('J.txt', 'r').readline()
line = sys.stdin.readlines()

words = re.split('\W+', line.strip())
for word in words:
    print(word)
