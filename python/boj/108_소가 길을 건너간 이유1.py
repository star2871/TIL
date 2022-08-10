import sys

sys.stdin = open("108_소가 길을 건너간 이유1.txt")

T =  int(input())
state = {}
cnt = 0
for tc in range(T):
    n, m = map(int, input().split())
    if n in state and state[n] != m:
        state[n] = m
        cnt += 1
    else:
        state[n] = m
print(cnt)
    