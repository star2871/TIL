import sys

sys.stdin = open("45_다이얼.txt")
""""""
# 첫번째방법
classify = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
s = input()
ans = 0
for c in s:
    for idx, dial in enumerate(classify):
        if c in dial:
            ans += 3 + idx
            break
print(ans)
""""""
""""""
# 두번째 방법
alp_to_num = {
    "A": 3,
    "B": 3,
    "C": 3,
    "D": 4,
    "E": 4,
    "F": 4,
    "G": 5,
    "H": 5,
    "I": 5,
    "J": 6,
    "K": 6,
    "L": 6,
    "M": 7,
    "N": 7,
    "O": 7,
    "P": 8,
    "Q": 8,
    "R": 8,
    "S": 8,
    "T": 9,
    "U": 9,
    "V": 9,
    "W": 10,
    "X": 10,
    "Y": 10,
    "Z": 10,
}

word = input()
time = 0
for i in word:
    time += alp_to_num.get(i)

print(time)
""""""
