import sys

sys.stdin = open("2072.txt")

T = int(input())

for tc in range(1, T+1):
    number = list(map(int,input().split()))
    result = 0
    for i in range(len(number)):
        if number[i] % 2 == 1:
            result += number[i]

    print(f'#{tc} {result}')