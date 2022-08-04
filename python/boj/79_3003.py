import sys


sys.stdin = open("79_3003.txt")
a = [1, 1, 2, 2, 2, 8]
chess_horse = list(map(int, input().split()))

for i in range(len(a)):
    print(a[i] - chess_horse[i], end = " ")
