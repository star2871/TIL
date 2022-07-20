import sys
sys.stdin = open("1986.txt", "r")

T = int(input())
for test_case in range(1, T + 1) :
    N = int(input())

    sum = 1
    for i in range(2, N+1) :
        if i%2 == 0 :
            sum -= i
        else :
            sum += i

    print(f'#{test_case} {sum}')