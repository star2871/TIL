import sys

sys.stdin = open("24_한수.txt")

n = int(input())
han = 0
for i in range(1, n + 1):
    if i < 100:
        han += 1
    else:
        ns = list(map(int, str(i)))
        # 일의자리와 십의자리차와 십의자리와 백의자리차같을때
        if ns[0] - ns[1] == ns[1] - ns[2]:
            han += 1
print(han)
