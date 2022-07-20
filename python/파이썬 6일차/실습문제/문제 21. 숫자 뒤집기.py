# import sys

# sys.stdin = open("문제 21.txt", "r")
# 쉬운방법
# number = int(input())

# print(int(str(number)[::-1]))

number = 123
result = 0
while number:
    #이전 결과에 10을 곱하고
    result *= 10
    # 나머지를 더해주고
    result += number%10
    # number를 깎는다.
    number //= 10
print(result)
