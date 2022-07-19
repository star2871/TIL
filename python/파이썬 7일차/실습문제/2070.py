import sys
sys.stdin = open("2070.txt", "r")

T = int(input())
for i in range(0, T):
        a, b = input().split()
        a = int(a)
        b = int(b)
        if a < b:
            print("#%d %s" %(i+1, '<'))
        elif a > b:
            print("#%d %s" %(i+1, '>'))
        else:
            print("#%d %s" %(i+1, '='))