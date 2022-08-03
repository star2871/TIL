import sys


sys.stdin = open("73_5와 6의 차이.txt")

a, b = input().split()

minimum = int(a.replace('6', '5')) + int(b.replace('6', '5'))
maximum = int(a.replace('5', '6')) + int(b.replace('5', '6'))
print(minimum, maximum)