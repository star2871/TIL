import sys

sys.stdin = open("52_카드.txt")

N = int(input())
d = {}
for i in range(N):
    n = int(input())
    d[n] = d.get(n, 0) + 1
li = sorted(d.items(), key=lambda x: (-x[1], x[0]))
print(li[0][0])
