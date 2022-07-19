import sys

sys.stdin = open("문제 21.txt", "r")

number = int(input())

print(int(str(number)[::-1]))
