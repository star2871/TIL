import sys

sys.stdin = open("26_최소, 최대.txt")



T = int(input())

n = list(map(int, input().split())) # 가로로 나열


print(min(n), max(n))