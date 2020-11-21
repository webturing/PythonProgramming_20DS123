a = [1, 1, 6, 3, 3]
b = [0] * 10
for x in a:
    b[x] += 1

for i in range(len(b)):
    if b[i] != 0:
        print(i, end=" ")
print()

for i in range(len(b)):
    if b[i] != 0:
        for j in range(b[i]):
            print(i, end=" ")
print()
