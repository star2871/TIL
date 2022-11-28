import sys

sys.stdin = open("60_배부른 마라토너.txt")

n = int(input())
a = dict()

for i in range(n):
    tmp = input().rstrip()
    if tmp not in a:
        a[tmp] = 1
    else:
        a[tmp] += 1
for i in range(n - 1):
    b = input().rstrip()
    a[b] -= 1
    if a[b] == 0:
        del a[b]
print(*a)
