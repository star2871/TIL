import sys, heapq

sys.stdin = open("boj_14235.txt")

n = int(input())
gift = []

for i in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0:
        if len(gift) == 0:
            print(-1)
        else:
            tmp = -heapq.heappop(gift)
            print(tmp)
    else:
        # 인풋 값에서 앞에 2는 갯수를 의미한다.
        for j in range(a[0]):
            heapq.heappush(gift, -a[j + 1])
