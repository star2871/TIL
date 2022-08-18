import sys

sys.stdin = open("1946.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    value = ""
    for i in range(1, n+1):
        a, b= list(input().split())
        b = int(b)
        value += a*b
        
    print(f'#{tc}')    
    for i in range(len(value)):
        if (i+1)%10 == 0:
            print(value[i])
        else:
            print(value[i], end="")
    print()