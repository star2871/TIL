import sys

sys.stdin = open("21_A+B - 5.txt")


while 1:
    a,b = map(int,input().split())
    if (a == 0 and b == 0):
        break
    else:
        print(a + b)
