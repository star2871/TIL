word = str(input())
for word_change in word:
    temp = word_change.replace("b", "B").replace("a", "A").replace("n", "N")
    print(temp)