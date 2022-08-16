import sys

sys.stdin = open("2_상수.txt")

A, B = input().split()
a = A[::-1]
b = B[::-1]

if a> b and a!=b:
    print(a)
else:
    print(b)

