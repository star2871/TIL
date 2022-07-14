word = str(input())
count_words = {}
for b in word:
    if b in count_words:
        count_words[b] += 1
    else :
        count_words[b] = 1
print(count_words)
    