n = 1007
flag = False
for c in range(2, n):
    if n % c == 0:
        flag = True
        break
if not flag :
    print(n, "is a primer")
else:
    print(n, "is a compositor")
