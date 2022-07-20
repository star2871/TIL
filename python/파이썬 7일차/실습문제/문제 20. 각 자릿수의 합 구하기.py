# import sys

# sys.stdin = open("문제 20.txt", "r")
number = int(input())
number = str(number)
sum=0
for i in range(0,len(number)):
    sum+=int(number[i])
print(sum)
