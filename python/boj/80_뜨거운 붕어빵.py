import sys


sys.stdin = open("80_뜨거운 붕어빵.txt")

n, m  = map(int, input().split())

for i in range(n):
    a =  input()
    reverse = a[::-1]
    print(reverse)