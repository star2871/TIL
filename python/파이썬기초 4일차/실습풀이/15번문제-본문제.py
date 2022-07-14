word = str(input())
is_a = False
for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        is_a = True
        break

if not is_a:
    print(-1)