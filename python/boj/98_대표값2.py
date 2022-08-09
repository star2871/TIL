import sys

sys.stdin = open("98_대표값2.txt")

list_n = []
for tc in range(5):
    n = int(input())
    list_n.append(n)
    list_n.sort()

print(sum(list_n)//5)
print(list_n[2])
    
    