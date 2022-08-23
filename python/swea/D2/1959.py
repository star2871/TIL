import sys

sys.stdin = open("1959.txt")

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    if n == m:
        max = 0
        for i in range(n):
            max +=a[i] * b[i]
    else:
        if n > m :
            sum = [0] * (n-m+1)
            for i in range(len(sum)):
                for j in range(-1, -m-1, -1):
                    sum[i] += a[j-i] * b[j]
        else:
            sum = [0] * (m-n+1)
            for i in range(len(sum)):
                for j in range(-1, -n-1, -1):
                    sum[i] += a[j] * b[j-i]
        sum.sort()
        max = sum[-1]

    print(f'#{tc} {max}')