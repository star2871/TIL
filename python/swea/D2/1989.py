# import sys

# sys.stdin = open("1989.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    
    # 단어가 정방향일때와 역방향일때에 
    # 같은단어가 나오면 0을 출력하고
    # 다른단어가 나오면 1을 출력한다.
    N = input().strip()
    if N == N[::-1]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')
