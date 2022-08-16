import sys

sys.stdin = open("10_별 찍기 - 20.txt")
n = int(input())
for i in range(n):
    if i%2 == 0:
        print('* '*n)
    else:
        print(' *'*n)
