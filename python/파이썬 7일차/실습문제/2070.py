# import sys
# sys.stdin = open("2070.txt", "r")

num = int(input())
for i in range(0, num):
        a, b = input().split()
        a = int(a)
        b = int(b)
        if a < b:
            print("#%d %s" %(i+1, '<'))
        elif a > b:
            print("#%d %s" %(i+1, '>'))
        else:
            print("#%d %s" %(i+1, '='))