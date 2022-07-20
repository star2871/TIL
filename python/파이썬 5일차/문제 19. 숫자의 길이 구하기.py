# 10 으로 나눈나머지로 하는방법
# def digit_length(n):
    # ans = 0
    # while n:
        # n //= 10
        # ans += 1

    # return ans
# print(digit_length(123))
# 1. 형변환 방법
# number = 123
# print(len(str(number)))
# 2. 123
# result = 0
# 몫이 0이 되면 종료해야하니까!
#while number != 0:
# while number:
    # number = number // 10
#    number //= 10
#    result += 1
# print(result)
# 3. log
# import math
# print(int(math.log(number, 10)) + 1)

