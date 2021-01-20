# coding=utf-8
s = ['Rocks', 'Papers', 'Scissors']
while True:
    a, b = input().strip().split()
    a = s.index(a)
    b = s.index(b)
    if a == b:
        print('draw')
    elif (a + 1) % 3 == b:
        print('lose')
    else:
        print('win')