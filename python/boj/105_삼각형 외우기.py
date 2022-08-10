import sys

sys.stdin = open("105_삼각형 외우기.txt")

a = int(input())
b = int(input())
c = int(input())

if a+b+c == 180 and a == b == c:
    print('Equilateral')
elif a+b+c == 180 and a == b or b == c or c == a:
    print('Isosceles')
elif a+b+c == 180 and a != b != c:
    print('Scalene')
elif a+b+c !=180:
    print('Error')