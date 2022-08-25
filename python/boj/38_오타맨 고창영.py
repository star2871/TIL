import sys

sys.stdin = open("38_오타맨 고창영.txt")

T = int(input())

for tc in range(1, T+1):
    n, m = input().split()
    n = int(n)
    print(m[:n-1], m[n:], sep='')
   