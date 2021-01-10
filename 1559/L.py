import sys, re


def comp(s):
    t = s.strip().split()
    return (int(t[1]), int(t[2]), int(t[3]),t[0])


lines = open('L.txt', 'r').readlines()
# lines = sys.stdin.readlines()

del lines[0]
persons = [line.strip() for line in lines if line.strip()]
persons = sorted(persons, key=lambda x:comp(x))
for person in persons:
    print(person.split()[0])
