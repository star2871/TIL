import sys

sys.stdin = open("96_모음의 개수.txt")

while True:
    word = input()
    if word == '#':
        break
    cnt = 0
    for c in word:
        if c in 'aeiouAEIOU':
            cnt += 1
    print(cnt)