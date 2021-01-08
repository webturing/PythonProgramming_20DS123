import sys
data = [line.strip() for line in sys.stdin.readlines()]
data = sorted(data, key=lambda t: (int(t[6:]),  int(t[0:2]), int(t[3:5])))
for date in data:
    print(date)
