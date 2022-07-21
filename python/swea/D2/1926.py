import sys

sys.stdin = open("1926.txt", "r")

T = int(input())

for test_case in range(1,T+1):
    # T = [3,6,9] 어느자리든 나올수있다.
    # 박수는 1번 2번 3번 칠수있다.
    cnt = 0
    temp = test_case
    # 0보다큰 양의정수
    while temp > 0:
        # 10으로 나누었을때 나머지가 3,6,9가나오는 경우를 다더한다.
        if temp % 10 in [3, 6, 9]:
            cnt += 1
        # 10으로 나누었을때 몫을 나타낸다.
        temp //= 10
    if cnt > 0:
        print("-"*cnt, end = " ")
    else:
        print(test_case, end = " ")