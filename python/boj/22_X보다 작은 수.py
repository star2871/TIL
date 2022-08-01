import sys

sys.stdin = open("22_X보다 작은 수.txt")

N, X = map(int, input().split())
num = list(map(int, input().split()))

for i in range(len(num)):
    if num[i] < X:
        print(num[i], end= " ")