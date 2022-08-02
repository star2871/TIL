import sys

sys.stdin = open("25_더하기 사이클.txt")

n = int(input())        # 26

num = n
cnt = 0                 # 사이클 수

while True:             # while 1이랑 동일
    a = num//10         # 2
    b = num%10          # 6
    c = (a+b)%10        # 8
    num = (b*10) +c     # 68
    cnt += 1
    if(num == n):
        break

print(cnt)
