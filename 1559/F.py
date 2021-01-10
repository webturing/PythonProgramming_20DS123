import sys

lines = open('F.txt', 'r').readlines()
#lines = sys.stdin.readlines()

data = [line.strip() for line in lines if line.strip()]
data = sorted(data, key=lambda t: (int(t[6:]), int(t[0:2]), int(t[3:5])))
for date in data: 
    print(date)
