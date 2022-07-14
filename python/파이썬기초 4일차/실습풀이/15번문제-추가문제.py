s = str(input())
c = 'a'
lst = []
for pos,char in enumerate(s):
    if(char == c):
        lst.append(pos)
print(lst)