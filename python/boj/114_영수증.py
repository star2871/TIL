import sys

sys.stdin = open("114.영수증.txt")

cost = int(input())
type = int(input())

sum = 0

for tc in range(type):
    n, m = map(int, input().split())
    sum += n*m
if cost == sum:
    print("Yes")
else:
    print("No")