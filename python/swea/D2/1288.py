# import sys

# sys.stdin = open("1288.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # xN번의 양을 세고있다.
    # N = 1일때
    # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    # 10N 까지 세면 다나온다.
    # N = 2일때
    # 2, 4, 6, 10, 12, 14, 16, 18, 20, 22, ... 90까지하면
    # 90N 까지 세면 다나온다.
    N = int(input())
    numbers = [0] * 10
    # 배수 올리기
    # i 가 0 이면 값이 나오지않는다.
    i = 1
    # numbers 0이 나올때부터
    while 0 in numbers:
        # num라는 변수에 N* i 를 문자취급한다.
        num = str(N* i)
        # 나오는 문자까지의 범위까지 반복한다.
        for j in range(len(num)):
            # 그 나온값의 문자열 자리를 정수로 변환하여 개수를 센다.
            numbers[int(num[j])] +=1
        i += 1
    print(f'#{test_case} {num}')


        
        
    
