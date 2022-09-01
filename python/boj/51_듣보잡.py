import sys

sys.stdin = open("51_듣보잡.txt")

N, M = map(int,input().split())


n =[input() for _ in range(N)]
m =[input() for _ in range(M)]

# & : 교집합
a = sorted(list(set(n)&set(m)))

print(len(a))
for i in a:
    print(i)


    