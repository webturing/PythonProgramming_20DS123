# coding=utf-8
n = int(input())
a = list(map(int, input().strip().split()))
s, e = map(int, input().strip().split())
print(sum(a[s - 1:e]))