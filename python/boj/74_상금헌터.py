import sys


sys.stdin = open("74_상금헌터.txt")

T = int(input())


def code1(a):
    if a == 1:
        return 5000000
    elif a > 1 and a < 4:
        return 3000000
    elif a > 3 and a < 7:
        return 200000
    elif a > 6 and a < 11:
        return 500000
    elif a > 10 and a < 16:
        return 300000
    elif a > 15 and a < 22:
        return 100000
    else:
        return 0
def code2(b):
    if b == 1:
        return 5120000
    elif b > 1 and b < 4:
        return 2560000
    elif b > 3 and b < 8:
        return 1280000
    elif b > 7 and b < 16:
        return 640000
    elif b > 15 and b < 32:
        return 320000
    else:
        return 0
for tc in range(T):
    a, b = map(int,input().split())    
    print(code1(a) + code2(b))