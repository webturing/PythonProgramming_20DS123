n=int(input().strip())
rank="F"
if n>=90 and n<=100:
    rank='A'
if n>=80 and n<90:
    rank='B'
if n>=70 and n<80:
    rank='C'
print(rank)

