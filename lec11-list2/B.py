F = [0] * 21

F[1] = F[2] = 1
for i in range(3, len(F)):
    F[i] = F[i - 1] + F[i - 2]
del F[0]
for e in F:
    print(e)
