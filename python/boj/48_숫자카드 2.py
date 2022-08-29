import sys

sys.stdin = open("48_숫자카드 2.txt")

A = int(input())
num_card = list(map(int,input().split()))
B = int(input())
card_number = list(map(int,input().split()))

for i in range(len(num_card)):
    print(num_card[i])
