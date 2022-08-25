import sys

sys.stdin = open("36_유학 금지.txt")


word = input()
censor = "CAMBRIDGE"
word_list = ""

for i in word:
    cnt = 0
    for j in censor:
        if i != j:
            cnt += 1
    # cnt == 9 라면 더이상 censor에있는 문자를 다뺀것이다.
    if cnt == 9:
        word_list += i
print(word_list)


