import sys

sys.stdin = open("115.와글와글숭고한.txt")

S, K , H = map(int, input().split())
if S+K+H >= 100:
    print("OK")
elif S < K and S < H:
    print("Soongsil")
elif K < S and K < H:
    print("Korea")
elif H < K and H < S:
    print("Hanyang")