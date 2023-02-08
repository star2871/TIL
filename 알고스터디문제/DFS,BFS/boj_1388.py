import sys

sys.stdin = open("boj_1388.txt")

n, m = map(int, input().split())
floor = []
for _ in range(n):
    w = input()
    w = list(w)
    floor.append(w)
cnt = 0
for i in range(n):
    if floor[i][0] == "-":
        cnt += 1
    for j in range(1, m):
        if floor[i][j] == "-" and floor[i][j - 1] == "|":
            cnt += 1

for i in range(m):
    if floor[0][i] == "|":
        cnt += 1
    for j in range(1, n):
        if floor[j][i] == "|" and floor[j - 1][i] == "-":
            cnt += 1

print(cnt)
