import sys

sys.stdin = open("연습.txt")

n = int(input())
num = list(map(int, input().split()))
cnt = 0
for i in range(0, len(num)):
    if num[i] == num[i - 1]:
        cnt += 1
        print(cnt)
    if num[i] != num[i - 1]:
        cnt = 1
if num[i] != num[i - 1]:
    not num[i] == num[i - 1]
    print(cnt)
