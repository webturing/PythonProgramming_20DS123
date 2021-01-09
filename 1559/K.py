import sys, re

line = open('K.txt', 'r').readline()
#line = sys.stdin.readlines()
freq = {}
words = re.split('\W+', line.strip())
words = sorted(words)
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(len(words))
for (k, v) in freq.items():
    print('%s:%d' % (k, v))
