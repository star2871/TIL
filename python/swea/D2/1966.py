import sys

sys.stdin = open("1966.txt")

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    m = list(map(int, input().split()))
    m.sort()

    print(f'#{tc}', end = ' ')
    for i in range(n):
        print(m[i], end =' ')

    print()