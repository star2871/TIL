import sys

sys.stdin = open("1959.txt")

T = int(input())

for tc in range(1, T+1):
    n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if n>= m:
        for i in range(1, n-m+n+1):

    elif n < m:
        for i in range(m-n+n, m-n):
    