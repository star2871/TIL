import sys

sys.stdin = open("107_콘테스트.txt")

list_a = []
for tc in range(10):
    a = int(input())
    list_a.append(a)
list_b = []
for tc in range(10):
    b = int(input())
    list_b.append(b)
list_a.sort(reverse=True)
list_b.sort(reverse=True)
list_asum = 0
list_bsum = 0

for tc in range(0,3):
    list_asum += list_a[tc]
    list_bsum += list_b[tc]
print(list_asum, list_bsum)
