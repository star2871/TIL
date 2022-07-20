# import sys
# sys.stdin = open("2071.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    numbers=list(map(int,input().split()))
    avg_value=sum(numbers)/len(numbers)
    avg_value=round(avg_value)
    print("#{} {}".format(test_case, avg_value))