# coding=utf-8
digits = map(int, list(input().strip()))
if sum(digits) % 2 == 0:
    print('yes')
else:
    print('no')
