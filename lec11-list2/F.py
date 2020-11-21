def circle(n):
    b = [0] * 10
    while n > 0:
        d = n % 10
        b[d] += 1
        n //= 10
    return b[0] + b[6] + b[9] + b[8] * 2


while True:
    n = int(input())
    print(circle(n))
