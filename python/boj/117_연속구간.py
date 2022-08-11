import sys

sys.stdin = open("117_연속구간.txt")


for tc in range(3):
    n = str(input())
    cnt = 1
    result = 1
    for tc in range(1,len(n)):
        if n[tc] == n[tc-1]:
            cnt += 1
        else:
            # 이부분 생각 못함
            result = max(cnt, result)
            cnt = 1
    result =  max(cnt, result)
    print(result)        
    
