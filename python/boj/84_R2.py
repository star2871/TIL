import sys


sys.stdin = open("84_R2.txt")

R1, S = map(int, input().split())
print(2*S-R1)