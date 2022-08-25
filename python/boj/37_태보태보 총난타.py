import sys

sys.stdin = open("37_태보태보 총난타.txt")

i = 0
r = [0, 0]
for c in input():
    if c == '@':
        # 왼쪽 1씩 더해지고 오른쪽 1씩 더해진다.
        r[i] += 1
    elif c == '(':
        # i ^= 1 == i += 1
        i += 1
# list 의 값을 뛰어쓰기하고 나온다.
print(*r)