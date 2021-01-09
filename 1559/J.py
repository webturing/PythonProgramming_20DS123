import sys
import re

line = open('J.txt', 'r').readline()
#line = sys.stdin.readline()

words = re.split('[^a-zA-Z]+', line.strip())

for word in words:
    print(word)
