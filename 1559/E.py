import sys
data = sorted(list(map(int, [x.strip() for x in sys.stdin.readlines() if x.strip()][1:])))
dic = {}
for d in data:
    if d in dic.keys():
        dic[d] += 1
    else:
        dic[d] = 1
mx = max(dic.values())
for k in dic.keys():
    if dic[k] == mx:
        print(k)
        print(mx)
