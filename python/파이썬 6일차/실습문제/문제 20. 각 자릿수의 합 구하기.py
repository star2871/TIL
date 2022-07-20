# import sys

# sys.stdin = open("문제 20.txt", "r")
# 나의 방법 문자취급하여 합하는거
# number = int(input())
# number = str(number)
# sum=0
# for i in range(0,len(number)):
#     sum+=int(number[i])
# print(sum)

# number = 123
# number가 0일 때 Stop!
# => int는 0일 때 False
# answer = 0
# while number:
    # 몫은 다음 number가됨.
    # 나머지는 더해나가면 된다!
    # 1.
#     answer += number%10
#     number //= 10
    # 2.
    # divmod(x, y)sms x를 y로 나누고,
    # 결과를 tuple로 반환
    # (몫, 나머지)
#     number, remainder = divmod(number, 10)
#     answer += remainder

# print(answer)