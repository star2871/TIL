import sys

sys.stdin = open("boj_1946.txt")

# 첫번째 방법
# input = sys.stdin.readline

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     rank = [list(map(int, input().split())) for _ in range(N)]
#     rank_asc = sorted(rank)
#     top = 0
#     result = 1

#     for i in range(1, len(rank_asc)):
#         if rank_asc[i][1] < rank_asc[top][1]:
#             top = i
#             result += 1

#     print(result)

# 두번째 방법

t = int(input())

for i in range(t):
    n = int(input())
    a = []
    for j in range(n):
        x, y = map(int, input().split())
        a.append([x, y])
    a.sort()

    L = a[0][1]
    index = 1
    for j in range(1, n):
        if a[j][1] < L:
            L = a[j][1]
            index += 1
    print(index)
