import sys

sys.stdin = open("2007.txt")

T = int(input())
cnt = 0
for tc in range(1, T+1):
    # 반복되는 단어의 갯수
    
    word = input()
    for i in range(1, 30) :
        # 어떤 자리의 글자가 첫번째 자리의 글자와 같을때
        if word[i] == word[0] :
            # 그 글자전까지 슬라이씽한게 그 글자에서 그 글자 2배만큼까지가 같을때
            if word[:i] == word[i:i*2] :
                #글자의 갯수를 더해 나간다. 또한 그다음에 없으면 멈춘다.
                cnt = i
                break
        if i == 29 :
            cnt = 30
    print(f'#{tc} {cnt}')
        