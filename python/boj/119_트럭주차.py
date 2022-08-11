import sys

sys.stdin = open("119_트럭주차.txt")

a, b, c = map(int, input().split())
# 이부분 생각 못함
list_i = [0]*101      
for tc in range(3):
    n, m = map(int, input().split())
    for i in range(n-1, m-1):
        # 이부분 생각 못함
        list_i[i] +=1 
answer = 0
for k in list_i:
    if k == 1:
        answer += a*k
    elif k == 2:
        answer += b*k
    elif k == 3:
        answer += c*k
print(answer)