import sys

sys.stdin = open("14_사분면 고르기.txt")

n = int(input())
m = int(input())

if n<0 and m>0:
    print(2)
elif n>0 and m>0:
    print(1)
elif n<0 and m<0:
    print(3)
else:
    print(4)