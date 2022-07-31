import sys
sys.stdin = open("2043.txt", "r")

a, b = list(map(int, input().split()))

print(a-b+1)

