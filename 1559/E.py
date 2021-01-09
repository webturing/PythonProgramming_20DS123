import sys

lines = open('E.txt', 'r').readlines()
#lines = sys.stdin.readlines()
del lines[0]
a = [int(line.strip()) for line in lines if line.strip()]
a = sorted(a)
freq = {}
for each in a:
    if each in freq:
        freq[each] += 1
    else:
        freq[each] = 1
max_freq = max(freq.values())
for (k, v) in freq.items():
    if v == max_freq:
        print(k)
        print(v)
        break
