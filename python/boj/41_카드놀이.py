import sys

sys.stdin = open("41_카드놀이.txt")

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ant = 0 # A의 점수
bnt = 0 # B의 점수

history = "D" # 승패 기록
for i in range(10):
    
    if A[i] == B[i] :
        ant +=1
        bnt +=1

    # A가 이길 경우    
    elif A[i] > B[i] :
        ant +=3
        history = "A"
    # B가 이길 경우    
    elif A[i] < B[i] :
        bnt +=3
        history = "B"

# A 스코어가 더 높을 경우
if ant > bnt:
    print(ant, bnt)
    print('A')

# B 스코어가 더 높을 경우
elif ant < bnt:
    print(ant, bnt)
    print('B')

# A, B 스코어가 같을 경우
if ant == bnt:

    if history == "A":    
        print(ant, bnt)
        print("A")
    if history == "B":    
        print(ant, bnt)
        print("B")
    if history == "D":    
        print(ant, bnt)
        print("D")