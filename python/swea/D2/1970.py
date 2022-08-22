import sys

sys.stdin = open("1970.txt")

list_won = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    list = [0] * 8
    for i in range(8):
        if n//list_won[i] != 0:
            list[i] = n//list_won[i]
            n = n%list_won[i]
    print(f'#{tc}')
    print(*list)