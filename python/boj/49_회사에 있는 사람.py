import sys

sys.stdin = open("49_회사에 있는 사람.txt")

import sys

n = int(sys.stdin.readline())

result = dict()
for _ in range(n):
    name, action = sys.stdin.readline().split()
    if action == "enter":
        result[name] = True
    else:
        del result[name]

print("\n".join(sorted(result.keys(), reverse=True)))
