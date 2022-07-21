# import sys

# sys.stdin = open("1976.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # 각각의 변수를 정수화하고 나열한다음에 list에 넣는다.
    N = list(map(int, input().split()))
    # a = N[0] + N[2]
    # b = N[1] + N[3]
    
    a = N[0] + N[2]
    b = N[1] + N[3]
    # b인분이 60이상이 될때 a인시간에 더하고 b에서 60을 뺀다.
    if b > 59:
        a += 1
        b = b - 60
    # a 13 이상이 될때 12를 빼서 시간을 나타낸다.
    if a > 12:
        a = a - 12
    
    print(f'#{test_case} {a} {b}')
