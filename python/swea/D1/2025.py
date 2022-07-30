import sys
sys.stdin = open("2025.txt", "r")

n = int(input())

cnt = 0
for tc in range(1,n+1):
    n = n+ cnt
    cnt +=1
print(n)
    