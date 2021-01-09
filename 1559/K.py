import sys, re

line = open('K.txt', 'r').readline()
#line = sys.stdin.readline()
freq = {}
words = re.split('\W+', line.lower().strip())
words = sorted(words)
for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(len(words))
for (k, v) in freq.items():
    print('%s:%d' % (k, v))
