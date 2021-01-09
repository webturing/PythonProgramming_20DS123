import sys, re


def comp(s):
    t = s.strip().split()
    return (t[1], t[2], t[3])


lines = open('L.txt', 'r').readlines()
# lines = sys.stdin.readlines()

del lines[0]
persons = [line.strip() for line in lines if line.strip()]
persons = sorted(persons, key=comp)
for person in persons:
    print(person.split()[0])
