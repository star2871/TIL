import sys

sys.stdin = open("56_2902.txt")

word = list(input().split('-'))

ans = ''
for i in word:
    ans+=i[0] # 각각의 인덱스의 첫번째를 말하는거다.
print(ans)


        