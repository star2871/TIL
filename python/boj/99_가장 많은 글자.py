import sys

sys.stdin = open("99_가장 많은 글자.txt")

eng = 'abcdefghijklmnopqrstuvwxyz'
word_list = []
for tc in range(14):
    word = input()
for i in eng:
    word_list.append(word.count(i))

    print(word_list)
# m = max(word_list)
# for i in range(len(word_list)):
#     if m == word_list[i]:
#         print(chr(i+97), end = '')

    