import sys

sys.stdin = open("3_OX 퀴즈.txt")

T = int(input())

for tc in range(1,T+1):
    ox = list(input())
    score = 0
    sum_score = 0
    for i in ox:
        if i == 'O':
            score += 1
            sum_score += score
        else:
            score = 0
    print(sum_score)