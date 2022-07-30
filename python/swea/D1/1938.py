import sys
sys.stdin = open("1938.txt", "r")

a, b = list(map(int, input().split()))
print(a+b)
print(a-b)
print(a*b)
print(a//b)



