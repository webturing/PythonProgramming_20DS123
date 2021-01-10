import sys, re, math

lines = open('W.txt', 'r').readlines()


# lines = sys.stdin.readlines()

def depth(exp):
    stack = []
    ans = 0
    for char in exp:
        if char == '(':
            stack.append(char)
            ans = max(ans, len(stack))
        elif char == ')':
            stack.pop(len(stack) - 1)
    return ans


for line in lines:
    if not line.strip(): continue
    print(depth(line))
