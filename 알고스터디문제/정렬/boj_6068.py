import sys

sys.stdin = open("boj_6068.txt")

# 여기 부분때문에 런타임애러 뜬다.
input = sys.stdin.readline
# 첫번째 방법
# N = int(input())
# works = [list(map(int, input().split())) for _ in range(N)]
# works = sorted(works, key=lambda x: x[1])
# total_time = 0
# min_rest = float("inf")
# for time, limit in works:
#     total_time += time
#     min_rest = min(min_rest, limit - total_time)
#     # 총시간이 더 커지는경우는 제외하기 위해서 넣었다.
#     if limit < total_time:
#         print(-1)
#         exit()
# print(min_rest)

# 두번째 방법
input = __import__("sys").stdin.readline
import sys

n = int(input())
l = []
for i in range(n):
    a, b = map(int, input().split())
    l.append((b, a))
l.sort(reverse=True)
last = l[0][0]
for i in l:
    last = min(last, i[0]) - i[1]
    if last < 0:
        print(-1)
        sys.exit()
print(last)
