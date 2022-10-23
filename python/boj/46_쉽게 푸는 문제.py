import sys

sys.stdin = open("46_쉽게 푸는 문제.txt")
""""""
# 이중 for문에다가 인덱스로 푸느법
A, B = list(map(int, input().split()))

arr = [0]
for i in range(46):
    for j in range(i):
        arr.append(i)

print(sum(arr[A : B + 1]))
""""""
""""""
# while 문을 이용한 방법
A, B = map(int, input().split())
count = 1
while True:
    if count**2 + count >= 2 * B:
        break
    else:
        count += 1

ans = []
for i in range(1, count + 1):
    ans.extend([i] * i)

print(sum(ans[A - 1 : B]))
""""""
