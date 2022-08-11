import sys

sys.stdin = open("118_애너그램.txt")

T = int(input())

for tc in range(1,T+1):
    a, b = list(map(str, input().split()))
    # 여기를 나눠서 생각 못함
    x = sorted(a)
    y = sorted(b)

    if x == y:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f"{a} & {b} are NOT anagrams.")