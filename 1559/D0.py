a = [0, 1, 2, -3]
a.sort()  # 默认是升序
a = sorted(a, key=lambda x: -x)  # 按照数值排降序
a = sorted(a, key=lambda x: abs(x))
a = sorted(a, key=abs)

a = sorted(a, key=lambda x: -abs(x))
a = sorted(a, key=abs)[::-1]

print(a)
