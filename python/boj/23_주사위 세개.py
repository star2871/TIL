import sys

sys.stdin = open("23_주사위 세개.txt")

x, y, z = list(map(int, input().split()))

if x == y == z:
    print(10000 + x*1000)

# elif x == y:
#     print(1000+x*100)
# elif x == z:
#     print(1000+x*100)
# elif y == z:
#     print(1000+y*100)
# 여기서 or 개념과 조건을 잘 사용해야한다.
elif x == y or x == z:
    print(1000 + x*100)
elif y == z:
    print(1000 + y*100)
else:
    print(max(x, y, z)*100)
